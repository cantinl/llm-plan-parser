import argparse
import plugins
import time

from gpt import generate_response
from config import PARSER_TEMPLATE

def parse_plan(domain_file, example_task_file, example_plan_file, task_description_file):
    template = PARSER_TEMPLATE
    with open(domain_file) as f:
        domain = f.read()
    with open(example_task_file) as f:
        example_task = f.read()
    with open(example_plan_file) as f:
        example_plan = f.read()
    with open(task_description_file) as f:
        task_description = f.read()
    
    prompt = template.format(domain, example_task, example_plan, task_description)

    interim_plan = generate_response(prompt)

    return interim_plan

    

def main():
    parser = argparse.ArgumentParser(description='Process domain file, problem file, and task description.')
    
    parser.add_argument('folder', help='Folder that all the files live in')
    parser.add_argument('domain_file', help='Path to the domain file')
    parser.add_argument('problem_file', help='Path to the problem file')
    parser.add_argument('task_description', help='Natural language description of the task')
    
    args = parser.parse_args()
    
    folder = args.folder
    domain_file = folder + '/' + args.domain_file
    problem_file = folder + '/' + args.problem_file
    task_description_file = folder + '/' + args.task_description
    example_plan_file = folder + '/' + 'p.sas'
    example_tasks_file = folder + '/' + 'p.steps'
    
    # Print the collected inputs
    print('Domain File:', domain_file)
    print('Problem File:', problem_file)
    print('Task Description:', task_description_file)
    
    interim_plan = parse_plan(domain_file, example_tasks_file, example_plan_file, task_description_file)
    tmp_file = f'/tmp/tmp_{time.time_ns()}.sas'
    with open(tmp_file, 'w') as f:
        f.write(interim_plan)

    print(interim_plan)

    pipeline = [
        plugins.RegexCheck(),
        plugins.ActionSymbolCheck(),
        plugins.ObjectCheck(),
        plugins.ParameterCheck(),
        plugins.GoalAchievementCheck()
    ]

    # Incremental pipeline
    # for i in range(len(plugins)):
    #     temp_pipeline = pipeline[:i+1]
    #     success = False
    #     while not success:
    #         for fnc in temp_pipeline:
    #             if not fnc(plan):
    #                 # Failure case
    #                 break
    #         # Success case
    #         success = True

    for check in pipeline:
        print(check)
        result, message = check.validate(domain_file, problem_file, None, tmp_file)
        if not result:
            print(message)
            exit(1)

    
    print("completed successfully")
    


if __name__ == '__main__':
    main()
