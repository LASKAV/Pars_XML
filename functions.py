import os


def push_github_pages():
    if not os.path.exists('data'):
        os.system('mkdir data')
    os.system('cd data && git init')
    os.system('cd data && git remote add promxls git@github.com:web-shark/promxls.github.io.git')
    os.system('cd data && git pull promxls master')
    os.system('cd data && git add .')
    os.system('cd data && git commit -m "data add from bot"')
    os.system('cd data && git push promxls master')