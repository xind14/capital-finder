# Lab: Class 16

## Author: Xin Deng

### Links and Resources

- chatGPT
- [requests](https://requests.readthedocs.io/en/latest/)
- [REST Countries API](https://restcountries.com/#rest-countries)
- [Vercel Python requirements](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Vercel CLI](https://vercel.com/docs/cli)

### Set up

Type into your terminal:

```bash
mkdir capital-finder
cd capital-finder
touch README.md
python3 -m venv .venv
source .venv/bin/activate
git init
touch .gitignore
mkdir api
touch api/capital-finder.py


```

Add `.venv` folder to `.gitignore`

```bash
git add .
git commit -m "first commit"
```

Create remote repo and follow instructions

```bash
pip freeze > requirements.txt
pip install requests
```

### Overview - Capital Finder

Capital Finder is a deployment of a serverless function to the cloud. It uses the requests library to interact with REST Countries API and following Vercel’s get-started directions that handles two kinds of queries:

- given a country name then responds with a string with the form The capital of X is Y
- given a capital then responds with a string with the form Y is the capital of X

#### Version 1.0

Build 1.0 Feature Tasks

1. Get request that handles a country name and responds with a string
2. Get request that handles a capital name and responds with a string
3. Use requests library to handle REST Countries API

### To run capital-finder:

1. Go to [Vercel site](https://capital-finder-xind14.vercel.app/)
2. Add pathway api/capital-finder?
3. Use queries of `country=` and `capital=`

## To test

1. Locally

    ```bash
    vercel dev
    ```

2. Remotely

- Test to look up a country: [https://capital-finder-xind14.vercel.app/api/capital-finder?country=Japan](https://capital-finder-xind14.vercel.app/api/capital-finder?country=Japan)

- Test to look up a capital: [https://capital-finder-xind14.vercel.app/api/capital-finder?capital=Tokyo](https://capital-finder-xind14.vercel.app/api/capital-finder?capital=Tokyo)
