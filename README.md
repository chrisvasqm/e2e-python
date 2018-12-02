# End-to-end Testing with Python

Sample project to showcase how to do E2E testing on a browser using Python.

## Test reports

In order to get `allure` test reports, run the following command on your terminal:

```
python3 -m pytest testcases/test_medium.py --alluredir=reports/
```

> _**Note**: make sure to execute this command from the root of the project._

## Steps

1. We will visit Medium's website.
2. Select the search icon.
3. Type in an username.
4. Filter the list of results by `People`.
5. Select the first result.
6. Verify that the user profile page is the one we expect by checking the URL.