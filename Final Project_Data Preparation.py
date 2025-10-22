# ---------------------------------------------------------
# If you are running in a Jupyter or Colab environment,
# install 'fredapi' first by uncommenting the following line:
# !pip install fredapi
# ---------------------------------------------------------

import pandas as pd
import numpy as np
from fredapi import Fred
import os

# 1. Your FRED API key
fred_api_key = "a051f637ff06f722b6837a28d9a45e85"
fred = Fred(api_key=fred_api_key)

# 2. Dictionary of ~100 FRED series (some may not be strictly "daily" or fully active)
fred_series_ids = {
    # 1–11: Treasury Constant Maturity Rates (Daily)
    "DGS1MO": "1-Month Treasury Constant Maturity Rate",
    "DGS3MO": "3-Month Treasury Constant Maturity Rate",
    "DGS6MO": "6-Month Treasury Constant Maturity Rate",
    "DGS1": "1-Year Treasury Constant Maturity Rate",
    "DGS2": "2-Year Treasury Constant Maturity Rate",
    "DGS3": "3-Year Treasury Constant Maturity Rate",
    "DGS5": "5-Year Treasury Constant Maturity Rate",
    "DGS7": "7-Year Treasury Constant Maturity Rate",
    "DGS10": "10-Year Treasury Constant Maturity Rate",
    "DGS20": "20-Year Treasury Constant Maturity Rate",
    "DGS30": "30-Year Treasury Constant Maturity Rate",

    # 12–14: T-Bill Secondary Market Rates (Daily)
    "DTB4WK": "4-Week Treasury Bill: Secondary Market Rate",
    "DTB3": "3-Month Treasury Bill: Secondary Market Rate",
    "DTB6": "6-Month Treasury Bill: Secondary Market Rate",

    # 15–19: Corporate Bond Spreads (Daily)
    "BAMLH0A0HYM2": "ICE BofA US High Yield Master II OAS",
    "BAMLCC0A1AA": "ICE BofA AAA US Corporate Index OAS",
    "BAMLCC0A3A": "ICE BofA Single-A US Corporate Index OAS",
    "BAMLCC0A4BBB": "ICE BofA BBB US Corporate Index OAS",
    "BAMLCC0A5BB": "ICE BofA BB US Corporate Index OAS",

    # 20–26: Federal Funds, Bank, and Repo Rates (Daily)
    "EFFR": "Effective Federal Funds Rate",
    "IORR": "Interest Rate on Reserve Balances (IORR)",
    "IOER": "Interest Rate on Excess Reserves (Discontinued)",
    "OBFR": "Overnight Bank Funding Rate",
    "SOFR": "Secured Overnight Financing Rate",
    "TEDRATE": "TED Spread",
    "RRPONTSYD": "Overnight Reverse Repurchase Agreements Award Rate",

    # 27–31: LIBOR (Daily)
    "USD1MTD156N": "1-Month LIBOR (USD)",
    "USD3MTD156N": "3-Month LIBOR (USD)",
    "USD6MTD156N": "6-Month LIBOR (USD)",
    "GBP1MTD156N": "1-Month LIBOR (GBP)",
    "GBP3MTD156N": "3-Month LIBOR (GBP)",

    # 32–45: Exchange Rates (Daily, “DEX” prefix from FRED)
    "DEXUSEU": "U.S. Dollar to Euro Exchange Rate",
    "DEXJPUS": "U.S. Dollar to Japanese Yen Exchange Rate",
    "DEXUSUK": "U.S. Dollar to U.K. Pound Sterling Exchange Rate",
    "DEXCAUS": "Canadian Dollar to U.S. Dollar Exchange Rate",
    "DEXCHUS": "Chinese Yuan to U.S. Dollar Exchange Rate",
    "DEXMXUS": "Mexican Peso to U.S. Dollar Exchange Rate",
    "DEXKOUS": "South Korean Won to U.S. Dollar Exchange Rate",
    "DEXBZUS": "Brazilian Real to U.S. Dollar Exchange Rate",
    "DEXARUS": "Argentine Peso to U.S. Dollar Exchange Rate",
    "DEXINUS": "Indian Rupee to U.S. Dollar Exchange Rate",
    "DEXSZUS": "Swiss Franc to U.S. Dollar Exchange Rate",
    "DEXSIUS": "Singapore Dollar to U.S. Dollar Exchange Rate",
    "DEXHKUS": "Hong Kong Dollar to U.S. Dollar Exchange Rate",
    "DEXTAUS": "New Taiwan Dollar to U.S. Dollar Exchange Rate",

    # 46–49: Additional Exchange Rates
    "DEXTHUS": "Thai Baht to U.S. Dollar Exchange Rate",
    "DEXSDUS": "Swedish Krona to U.S. Dollar Exchange Rate",
    "DEXSLUS": "Sri Lankan Rupee to U.S. Dollar Exchange Rate",
    "DEXNOUS": "Norwegian Krone to U.S. Dollar Exchange Rate",

    # 50–54: Key Commodities (Daily)
    "DCOILWTICO": "Crude Oil Prices: WTI",
    "DCOILBRENTEU": "Crude Oil Prices: Brent - Europe",
    "GOLDAMGBD228NLBM": "Gold Fixing Price 10:30 A.M. (London)",
    "SLVPRUSD": "Silver Price (check if truly daily)",
    "DHHNGSP": "Henry Hub Natural Gas Spot Price",

    # 55: Jet Fuel (Daily)
    "DJFUELUSGULF": "U.S. Gulf Coast Kerosene-Type Jet Fuel Spot Price",

    # 56–60: Equity Indexes (Daily)
    "SP500": "S&P 500 Index",
    "VIXCLS": "CBOE Volatility Index (VIX)",
    "NASDAQCOM": "NASDAQ Composite Index",
    "DJIA": "Dow Jones Industrial Average",
    "WILL5000IND": "Wilshire 5000 Total Market Index",

    # 61–65: ICE BofA Corporate Yields (Daily)
    "BAMLC0A1CAAAEY": "ICE BofA AAA US Corp Index Effective Yield",
    "BAMLC0A2CAAEY": "ICE BofA AA US Corp Index Effective Yield",
    "BAMLC0A3CAEY": "ICE BofA Single-A US Corp Index Effective Yield",
    "BAMLC0A4CBBBEY": "ICE BofA BBB US Corp Index Effective Yield",
    "BAMLH0A0HYBBEY": "ICE BofA US High Yield Master II Effective Yield",

    # 66: Bank Prime Loan Rate (Daily updates only when changed)
    "DPRIME": "Bank Prime Loan Rate",

    # 67–71: More LIBOR variants (Daily)
    "GBP6MTD156N": "6-Month LIBOR (GBP)",
    "CHF3MTD156N": "3-Month LIBOR (CHF)",
    "JPN3MTD156N": "3-Month LIBOR (JPY)",
    "EUR3MTD156N": "3-Month LIBOR (EUR)",
    "USDONTD156N": "Overnight LIBOR (USD)",

    # 72–76: Additional “DEX” exchange rates
    "DEXDNUS": "Danish Krone to U.S. Dollar Exchange Rate",
    "DEXALUS": "Albanian Lek to U.S. Dollar Exchange Rate",
    "DEXCZHUS": "Czech Koruna to U.S. Dollar Exchange Rate",
    "DEXMAUS": "Moroccan Dirham to U.S. Dollar Exchange Rate",
    "DEXPLUS": "Polish Zloty to U.S. Dollar Exchange Rate",

    # 77–79: More daily rates/spreads
    "BAMLH0A1CAAEY": "ICE BofA CCC & Lower US High Yield Index Effective Yield",
    "T10YIE": "10-Year Breakeven Inflation Rate",
    "T5YIE": "5-Year Breakeven Inflation Rate",

    # 80–82: Treasury Inflation-Indexed Security (TIPS) Yields (Daily)
    "DFII5": "5-Year TIPS Yield",
    "DFII10": "10-Year TIPS Yield",
    "DFII30": "30-Year TIPS Yield",

    # 83–92: ICE Swap Rates (Daily, if available)
    "ICERATES1100USD1Y": "1-Year ICE Swap Rate (USD)",
    "ICERATES1100USD2Y": "2-Year ICE Swap Rate (USD)",
    "ICERATES1100USD3Y": "3-Year ICE Swap Rate (USD)",
    "ICERATES1100USD5Y": "5-Year ICE Swap Rate (USD)",
    "ICERATES1100USD7Y": "7-Year ICE Swap Rate (USD)",
    "ICERATES1100USD10Y": "10-Year ICE Swap Rate (USD)",
    "ICERATES1100USD30Y": "30-Year ICE Swap Rate (USD)",
    "BAMLH0A3HYCEY": "ICE BofA Single-B US High Yield Index Effective Yield",
    "T20YIEM": "20-Year Breakeven Inflation Rate (check freq)",
    "DHOILNYH": "No. 2 Heating Oil, New York Harbor (check daily)",

    # 93–100: Fillers (some not daily!)
    "DGASSP": "Gasoline Spot Price (US Average, check freq)",
    "MICH": "U of Michigan: Consumer Sentiment (likely monthly)",
    "ICSA": "Initial Jobless Claims (weekly)",
    "WALCL": "Fed Assets (weekly)",
    "CPIAUCSL": "CPI for All Urban Consumers (monthly)",
    "GS10": "10-Year Treasury (alias for DGS10?)",
    "T7YIE": "7-Year Breakeven Inflation Rate (check freq)",
    "PNAPETHUSDM": "Palladium Price (check freq)"
}

# 3. Define the date range for the last 10 year
end_date = pd.Timestamp.today().normalize()
start_date = end_date - pd.Timedelta(days=3650)

# 4. Create a date index for daily frequency over the last year
date_index = pd.date_range(start=start_date, end=end_date, freq='D')

# 5. Create an empty DataFrame with this daily index to combine all valid series
combined_df = pd.DataFrame(index=date_index)

for series_id, description in fred_series_ids.items():
    print(f"Downloading {series_id} ({description})...")
    try:
        # Fetch data for the last year
        data = fred.get_series(
            series_id,
            observation_start=start_date.strftime('%Y-%m-%d'),
            observation_end=end_date.strftime('%Y-%m-%d')
        )

        # If there's no data returned at all, skip
        if data is None or data.empty:
            print(f" -> No data returned for {series_id}, skipping.\n")
            continue

        # Put into a DataFrame and reindex to daily
        df_series = pd.DataFrame(data, columns=[series_id])
        df_series.index.name = "DATE"
        df_series = df_series.reindex(combined_df.index)  # do not fill yet

        '''# Check how many missing values (before fill)
        missing_count = df_series[series_id].isna().sum()
        if missing_count > 100:
            print(f" -> {series_id} has {missing_count} NaNs (>100). Dropping.\n")
            continue

        # Forward-fill now
        df_series.ffill(inplace=True)

        # If after filling, all remain NaN, skip
        if df_series[series_id].isna().all():
            print(f" -> {series_id} is still all NaN after ffill, skipping.\n")
            continue
        '''
        # Otherwise, add this to the combined DataFrame
        combined_df[series_id] = df_series[series_id]
        print(f" -> {series_id} added.\n")
    except Exception as e:
        print(f"Failed to download {series_id}. Error: {e}\n")

# 6. Forward-fill the entire DataFrame again for any partial NaNs
combined_df.ffill(inplace=True)

# 7. Save to a single CSV
output_filename = "fred_combined_10yrs.csv"
combined_df.to_csv(output_filename, index_label="DATE")

print(f"All done! Data for valid FRED series saved to '{output_filename}'.")
