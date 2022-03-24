# import string
# import time
# from datetime import datetime
# from typing import Generator
#
# import pandas
# from numpy import random
#
#
# class ThePandas:
#
#     def __init__(self):
#         self.file_path_results = f"files/results"
#         self.list_symbols = [symbol for symbol in string.ascii_lowercase]
#
#     def save_to_cvs(self, dataset, filename):
#         dataset.to_csv(f'{self.file_path_results}/{filename}.csv', sep='\t', encoding='utf-8')
#
#     def get_generate_rows(self, count_rows: int) -> Generator:
#         return (self.__get_random_row() for _ in range(count_rows))
#
#     def __get_random_row(self) -> str:
#         return f"{self.__get_random_lower_string(10)}," \
#                f"{self.__get_random_lower_string(10)}," \
#                f"{self.__get_random_date_time()}," \
#                f"{self.__get_random_lower_string(5)}{self.__get_random_mail_sub_domain()}"
#
#     def __get_random_lower_string(self, count_symbols: int) -> str:
#         return ''.join(self.get_random_str(count_symbols))
#
#     def __get_random_date_time(self) -> str:
#         return datetime.fromtimestamp(random.randint(1, int(time.time()))).strftime('%Y-%m-%d %H:%M:00')
#
#     def __get_random_mail_sub_domain(self) -> str:
#         return random.choice(('@mail.ru', '@gmail.com', '@yandex.ru'))
#
#     def get_random_str(self, count_symbols: int):
#         random.shuffle(self.list_symbols)
#         return self.list_symbols[:count_symbols]
#
#
# if __name__ == '__main__':
#     start = time.time()
#     pd = ThePandas()
#     df = pandas.DataFrame(data={"res": pd.get_generate_rows(500000)})
#     print("prepare data: ", time.time() - start)
#     pd.save_to_cvs(df, "tmp")
#     print("end_save_scv:", time.time() - start)
