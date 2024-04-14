# ���������

��� ������ ����� ������� ��������� ���������� ��������� ����������:
- `selenium`
- `pytest`

�� ������ ���������� �� � ������� ������� pip:

### _��������� Selenium_
- `pip install selenium`

Selenium ������� ���� chromedriver.exe, � ��� ����� �����, ��� ��� �����. ����� ���� ��������� ��������� ��������, �� ������� ������� ��� � ���������� PATH Windows, ��� ������� � ������������ Selenium.

�������� ��������� �����, ���������� �� � C:\WebDriver\bin\. ����� ��������� ��� � ��������� ������ Windows:

- `setx PATH "%PATH%;C:\WebDriver\bin"`

### _��������� Pytest_
- `pip install pytest` - ��� ��������� pytest


# ������ ������

1. ### �������� �������� � �������� ����� �����������.

2. ### ��������� ����� � ������� �������:
- `pytest test_avito_count.py`
- `pytest -v test_avito_count.py` - ��� ��������� ������������ �� ������� �� ������

3. ### **��������� ����������**

- ����� ���������� ������ ��������� ����� output ��� ����������� ����������.

- ��� �������� ���������� ������ ��������� ��������� ����� ��������� � ����� output.

- ���� ����� �� ������ ��-�� ���������� ��������� �� ��������, ��������� �� ������� ����� ��������� � ����� BUGS.md.


##### �������������� ����������
� ������ ������������� ������� ��� ��������, ����������, ���������� � [������������ Selenium WebDriver](https://selenium-python.readthedocs.io/index.html).

��� ������������� ����� ��������� ������ ��������� ������� ��������, ����� ��� ������ ���� � ����� headless, � ����� test_avito_count.py.