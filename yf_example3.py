""" yf_example3.py

Summary: Code challenge for downloading stock prices
"""

import os

import toolkit_config as cfg

import yf_example2

# Download Qantas stock prices for a given year into a CSV file
def qan_prc_to_csv(year):
    """ Download Qantas stock prices for a given year into a CSV file

        Parameters
        ----------
        year : int
            year of desired stock prices for QANTAS

        """
    filename = f'qan_prc_{year}.csv'
    pth = os.path.join(cfg.DATADIR, filename)
    yf_example2.yf_prc_to_csv('QAN.AX', pth, f'{year}-01-01', f'{year}-12-31')

# Test case
if __name__ == "__main__":
    qan_prc_to_csv(2020)