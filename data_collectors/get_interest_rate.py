import pandas as pd
import quandl
import requests
from load_key import decrypt_api_key

def get_federal_funds_rate(api_key: str):
    """
    English:
    Fetches the historical Federal Funds Rate (FFUNDS) data from Nasdaq Data Link.

    Parameters:
    - api_key: str, Nasdaq Data Link API key

    Returns:
    - DataFrame: A pandas DataFrame containing the Federal Funds Rate data

    Korean:
    Nasdaq Data Link에서 연방 기금 금리(FFUNDS) 데이터를 가져옵니다.

    매개변수:
    - api_key: str, Nasdaq Data Link API 키

    반환값:
    - DataFrame: 연방 기금 금리 데이터를 포함하는 pandas DataFrame
    """
    url = f"https://data.nasdaq.com/api/v3/datasets/FRED/FFUNDS.json?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data['dataset']['data'], columns=data['dataset']['column_names'])
        df.set_index('Date', inplace=True)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Load and decrypt the API key
    # API 키를 로드하고 복호화합니다.
    with open("security/api_encrypted.txt", "rb") as file:
        encrypted_key = file.read()
    api_key = decrypt_api_key(encrypted_key)
    
    # Fetch Federal Funds Rate data
    # 연방 기금 금리 데이터를 가져옵니다.
    df = get_federal_funds_rate(api_key)
    if df is not None:
        df.to_csv('data/federal_funds_rate.csv')
        print("Data saved to federal_funds_rate.csv")
    else:
        print("Failed to fetch Federal Funds Rate data.")