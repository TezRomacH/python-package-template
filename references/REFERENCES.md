# REFERENCES

## repos
| full_name                                                                                                             | created_at          | updated_at          | size | stargazers_count |   |
|-----------------------------------------------------------------------------------------------------------------------|---------------------|---------------------|------|------------------|---|
| [TezRomacH/python-package-template](https://api.github.com/repos/TezRomacH/python-package-template)                   | 2020-04-15 14:53:29 | 2022-07-17 4:12:04  | 1318 | 763              |   |
| [audreyfeldroy/cookiecutter-pypackage](https://api.github.com/repos/audreyfeldroy/cookiecutter-pypackage)             | 2013-07-14 18:52:05 | 2022-07-17 2:31:21  | 557  | 3539             |   |
| [boromir674/cookiecutter-python-package](https://api.github.com/repos/boromir674/cookiecutter-python-package)         | 2022-04-21 1:33:49  | 2022-07-04 11:48:59 | 451  | 3                |   |
| [simonw/click-app-template-repository](https://api.github.com/repos/simonw/click-app-template-repository)             | 2021-08-30 1:03:34  | 2022-07-17 2:01:39  | 12   | 8                |   |
| [timhughes/cookiecutter-poetry](https://api.github.com/repos/timhughes/cookiecutter-poetry)                           | 2020-09-22 15:08:49 | 2022-07-04 8:11:05  | 117  | 5                |   |
| [waynerv/cookiecutter-pypackage](https://api.github.com/repos/waynerv/cookiecutter-pypackage)                         | 2021-05-19 9:43:34  | 2022-07-16 3:21:52  | 984  | 44               |   |
| [zillionare/python-project-wizard](https://api.github.com/repos/zillionare/python-project-wizard)                     | 2021-04-10 14:46:32 | 2022-06-28 9:15:24  | 946  | 55               |   |
| [william-cass-wright/cookiecutter-click-app](https://api.github.com/repos/william-cass-wright/cookiecutter-click-app) | 2022-06-20 6:53:50  | 2022-07-17 5:58:45  | 37   | 0                |   |
| [william-cass-wright/cookiecutter-pypackage](https://api.github.com/repos/william-cass-wright/cookiecutter-pypackage) | 2022-07-14 8:45:28  | 2022-07-17 5:52:53  | 984  | 0                |   |


## topics
| name                          | mkdocstrings | pyinstaller | cookiecutter-poetry | github-ci | tox   | cookiecutter | best-practices |
|-------------------------------|--------------|-------------|---------------------|-----------|-------|--------------|----------------|
| click-app-template-repository | -        | -       | -               | -     | - | -        | -          |
| cookiecutter-click-app        | -        | -       | -               | -     | - | -        | -          |
| cookiecutter-poetry           | -        | TRUE        | TRUE                | -     | - | TRUE         | -          |
| cookiecutter-pypackage        | -        | -       | -               | -     | - | -        | -          |
| cookiecutter-pypackage        | -        | -       | -               | -     | - | -        | -          |
| cookiecutter-pypackage        | -        | -       | -               | -     | - | -        | -          |
| cookiecutter-python-package   | -        | -       | -               | -     | - | TRUE         | -          |
| python-package-template       | -        | -       | -               | -     | - | TRUE         | TRUE           |
| python-project-wizard         | TRUE         | -       | -               | TRUE      | TRUE  | TRUE         | -          |

**continued...**
| codecov | jupyterlab | automated-testing | ci    | cookiecutter-python | cookiecutter-pypi-package | cookiecutter-python3 | cookiecutter-pypackage | pre-commit-hooks | python | automation | pypi-package |
|---------|------------|-------------------|-------|---------------------|---------------------------|----------------------|------------------------|------------------|--------|------------|--------------|
| -   | -      | -             | - | -               | -                     | -                | -                  | -            | -  | -      | -        |
| -   | -      | -             | - | -               | -                     | -                | -                  | -            | -  | -      | -        |
| -   | TRUE       | -             | - | -               | -                     | -                | -                  | -            | TRUE   | -      | -        |
| -   | -      | -             | - | -               | -                     | -                | -                  | -            | -  | -      | -        |
| -   | -      | -             | - | -               | -                     | -                | -                  | -            | -  | -      | -        |
| -   | -      | -             | - | -               | -                     | -                | -                  | -            | -  | -      | -        |
| -   | -      | TRUE              | TRUE  | TRUE                | TRUE                      | -                | -                  | -            | -  | TRUE       | TRUE         |
| -   | -      | -             | - | -               | -                     | -                | -                  | -            | TRUE   | -      | -        |
| TRUE    | -      | -             | - | -               | -                     | TRUE                 | TRUE                   | TRUE             | TRUE   | -      | -        |

**continued...**
| makefile | template | codestyle | pytest | scaffold | semantic-versions | cookiecutter-template | boilerplate | python-packages |
|----------|----------|-----------|--------|----------|-------------------|-----------------------|-------------|-----------------|
| -    | -    | -     | -  | -    | -             | -                 | -       | -           |
| -    | -    | -     | -  | -    | -             | -                 | -       | -           |
| -    | -    | -     | TRUE   | -    | -             | TRUE                  | -       | -           |
| -    | -    | -     | -  | -    | -             | -                 | -       | -           |
| -    | -    | -     | -  | -    | -             | -                 | -       | -           |
| -    | -    | -     | -  | -    | -             | -                 | -       | -           |
| -    | -    | -     | -  | -    | -             | TRUE                  | -       | -           |
| TRUE     | TRUE     | TRUE      | -  | -    | TRUE              | -                 | -       | TRUE            |
| -    | TRUE     | -     | -  | TRUE     | -             | TRUE                  | TRUE        | -           |

## code
```python
import datetime

import pandas as pd
from github import Github

def get_attrs(repo, attrs):
    return [getattr(repo,attr) if not isinstance(getattr(repo,attr),datetime.datetime) else str(getattr(repo,attr)) for attr in attrs]

def get_attr_fns(repo, attrs):
    return [getattr(repo,attr)() if not isinstance(getattr(repo,attr)(),datetime.datetime) else str(getattr(repo,attr)()) for attr in attrs]

def get_page_fns(repo, attrs):
    for attr in attrs:
        labels = []
        for label in getattr(repo,attr)():
            labels.append(getattr(label,attrs[attr]))
    return [labels]

def get_release(repo):
    try:
        x = getattr(repo,'get_latest_release')()
        return [getattr(x,'title')]
    except Exception as e:
        print(e)
        return ["NA"]

def get_gh_info(g, repo_name, attrs, attr_fns, attr_page_fns):
    repo_name = repo_name.replace("https://github.com/","")
    repo = g.get_repo(repo_name)
    print(repo.name)
    return get_attrs(repo,attrs) + get_attr_fns(repo,attr_fns) + get_page_fns(repo,attr_page_fns) + get_release(repo)

def get_set(field_name, df):
    return list(set([item for sublist in list(df[field_name]) for item in sublist]))

def get_github_data():
    access_token = "<access_token>"
    g = Github(access_token)

    repos = [
        'https://github.com/william-cass-wright/cookiecutter-pypackage-slim',
        'https://github.com/audreyfeldroy/cookiecutter-pypackage',
        'https://github.com/boromir674/cookiecutter-python-package',
        'https://github.com/simonw/click-app-template-repository',
        'https://github.com/timhughes/cookiecutter-poetry',
        'https://github.com/waynerv/cookiecutter-pypackage',
        'https://github.com/zillionare/python-project-wizard',
        'https://github.com/william-cass-wright/cookiecutter-click-app',
        'https://github.com/william-cass-wright/cookiecutter-pypackage',
        'https://github.com/briggySmalls/cookiecutter-pypackage',
    ]

    attrs = [
        "name",
        "full_name",
        "created_at",
        "updated_at",
        "url",
        "description",
        "private",
        "size",
        "stargazers_count",
        "forks",
    ]

    attr_fns = [
        "get_topics",
        # "get_release",
    ]

    attr_page_fns = {
        "get_labels":"name",
        # "get_latest_release":"title",
        # "get_forks",
    }


    res = []
    for repo_name in repos:
        try:
            res.append(get_gh_info(g, repo_name, attrs, attr_fns, attr_page_fns))
        except Exception as e:
            print(e)

    df = pd.DataFrame(res)
    df.columns = attrs + attr_fns + list(attr_page_fns) + ['get_latest_release']

    filename = f'{str(datetime.date.today())}-github-projects.csv'
    df.to_csv(filename, index=False)
    return df

def main():
    df = get_github_data()

    tables = []
    field_names = ['get_topics','get_labels']
    for field in field_names:
        cols = get_set(field, df)
        table = []
        for i in range(len(df)):
            res = []
            repo_name = df.iloc[i]['name']
            res.append(repo_name)
            for col in cols:
                if col in df.iloc[i][field]:
                    res.append(True)
                else:
                    res.append(False)
            table.append(res)
        ndf = pd.DataFrame(table)
        ndf.columns = ['name']+cols
        filename = f'{str(datetime.date.today())}-github-projects-{field}.csv'
        ndf.to_csv(filename, index=False)
    return df
    
df = main()
```