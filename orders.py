{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a31a5f75-d645-45f2-b7b5-0da4257378ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: kaggle in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (1.7.4.2)\n",
      "Requirement already satisfied: bleach in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (4.1.0)\n",
      "Requirement already satisfied: certifi>=14.05.14 in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (2025.1.31)\n",
      "Requirement already satisfied: charset-normalizer in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (3.3.2)\n",
      "Requirement already satisfied: idna in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (3.7)\n",
      "Requirement already satisfied: protobuf in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (4.25.3)\n",
      "Requirement already satisfied: python-dateutil>=2.5.3 in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (2.9.0.post0)\n",
      "Requirement already satisfied: python-slugify in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (5.0.2)\n",
      "Requirement already satisfied: requests in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (2.32.3)\n",
      "Requirement already satisfied: setuptools>=21.0.0 in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (75.1.0)\n",
      "Requirement already satisfied: six>=1.10 in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (1.16.0)\n",
      "Requirement already satisfied: text-unidecode in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (1.3)\n",
      "Requirement already satisfied: tqdm in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (4.66.5)\n",
      "Requirement already satisfied: urllib3>=1.15.1 in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (2.2.3)\n",
      "Requirement already satisfied: webencodings in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from kaggle) (0.5.1)\n",
      "Requirement already satisfied: packaging in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from bleach->kaggle) (24.1)\n",
      "Requirement already satisfied: colorama in c:\\users\\pmdar\\anaconda3\\lib\\site-packages (from tqdm->kaggle) (0.4.6)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install kaggle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8e48d1bd-5d43-4375-88ce-78304ecbb069",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dataset URL: https://www.kaggle.com/datasets/ankitbansal06/retail-orders\n",
      "Downloading orders.csv to ./data\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|████████████████████████████████████████████████████████████████████████████████| 200k/200k [00:00<00:00, 175MB/s]"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Dataset downloaded successfully!\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "import kaggle\n",
    "\n",
    "# Define the dataset name\n",
    "dataset = \"ankitbansal06/retail-orders\"\n",
    "file_name = \"orders.csv\"\n",
    "\n",
    "# Download the dataset\n",
    "kaggle.api.dataset_download_file(dataset, file_name, path=\"./data\", force=True)\n",
    "\n",
    "print(\"Dataset downloaded successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "3db758d5-6df2-46b8-a2b2-6f94b1cc5234",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dataset URL: https://www.kaggle.com/datasets/ankitbansal06/retail-orders\n",
      "License(s): CC0-1.0\n"
     ]
    }
   ],
   "source": [
    "!kaggle datasets download ankitbansal06/retail-orders -p ./data --unzip\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "6537ea27-0f7d-49a1-b4ce-d32945856a79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order Id</th>\n",
       "      <th>Order Date</th>\n",
       "      <th>Ship Mode</th>\n",
       "      <th>Segment</th>\n",
       "      <th>Country</th>\n",
       "      <th>City</th>\n",
       "      <th>State</th>\n",
       "      <th>Postal Code</th>\n",
       "      <th>Region</th>\n",
       "      <th>Category</th>\n",
       "      <th>Sub Category</th>\n",
       "      <th>Product Id</th>\n",
       "      <th>cost price</th>\n",
       "      <th>List Price</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Discount Percent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2023-03-01</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Henderson</td>\n",
       "      <td>Kentucky</td>\n",
       "      <td>42420</td>\n",
       "      <td>South</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Bookcases</td>\n",
       "      <td>FUR-BO-10001798</td>\n",
       "      <td>240</td>\n",
       "      <td>260</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2023-08-15</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Henderson</td>\n",
       "      <td>Kentucky</td>\n",
       "      <td>42420</td>\n",
       "      <td>South</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Chairs</td>\n",
       "      <td>FUR-CH-10000454</td>\n",
       "      <td>600</td>\n",
       "      <td>730</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2023-01-10</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>United States</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>California</td>\n",
       "      <td>90036</td>\n",
       "      <td>West</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Labels</td>\n",
       "      <td>OFF-LA-10000240</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2022-06-18</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Fort Lauderdale</td>\n",
       "      <td>Florida</td>\n",
       "      <td>33311</td>\n",
       "      <td>South</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Tables</td>\n",
       "      <td>FUR-TA-10000577</td>\n",
       "      <td>780</td>\n",
       "      <td>960</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2022-07-13</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Fort Lauderdale</td>\n",
       "      <td>Florida</td>\n",
       "      <td>33311</td>\n",
       "      <td>South</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Storage</td>\n",
       "      <td>OFF-ST-10000760</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Order Id  Order Date       Ship Mode    Segment        Country  \\\n",
       "0         1  2023-03-01    Second Class   Consumer  United States   \n",
       "1         2  2023-08-15    Second Class   Consumer  United States   \n",
       "2         3  2023-01-10    Second Class  Corporate  United States   \n",
       "3         4  2022-06-18  Standard Class   Consumer  United States   \n",
       "4         5  2022-07-13  Standard Class   Consumer  United States   \n",
       "\n",
       "              City       State  Postal Code Region         Category  \\\n",
       "0        Henderson    Kentucky        42420  South        Furniture   \n",
       "1        Henderson    Kentucky        42420  South        Furniture   \n",
       "2      Los Angeles  California        90036   West  Office Supplies   \n",
       "3  Fort Lauderdale     Florida        33311  South        Furniture   \n",
       "4  Fort Lauderdale     Florida        33311  South  Office Supplies   \n",
       "\n",
       "  Sub Category       Product Id  cost price  List Price  Quantity  \\\n",
       "0    Bookcases  FUR-BO-10001798         240         260         2   \n",
       "1       Chairs  FUR-CH-10000454         600         730         3   \n",
       "2       Labels  OFF-LA-10000240          10          10         2   \n",
       "3       Tables  FUR-TA-10000577         780         960         5   \n",
       "4      Storage  OFF-ST-10000760          20          20         2   \n",
       "\n",
       "   Discount Percent  \n",
       "0                 2  \n",
       "1                 3  \n",
       "2                 5  \n",
       "3                 2  \n",
       "4                 5  "
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load the dataset\n",
    "df = pd.read_csv(\"./data/orders.csv\")\n",
    "\n",
    "# Display first few rows\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "283ef0fe-8c8b-4c0b-895f-65ca5a11d158",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 9994 entries, 0 to 9993\n",
      "Data columns (total 16 columns):\n",
      " #   Column            Non-Null Count  Dtype \n",
      "---  ------            --------------  ----- \n",
      " 0   Order Id          9994 non-null   int64 \n",
      " 1   Order Date        9994 non-null   object\n",
      " 2   Ship Mode         9993 non-null   object\n",
      " 3   Segment           9994 non-null   object\n",
      " 4   Country           9994 non-null   object\n",
      " 5   City              9994 non-null   object\n",
      " 6   State             9994 non-null   object\n",
      " 7   Postal Code       9994 non-null   int64 \n",
      " 8   Region            9994 non-null   object\n",
      " 9   Category          9994 non-null   object\n",
      " 10  Sub Category      9994 non-null   object\n",
      " 11  Product Id        9994 non-null   object\n",
      " 12  cost price        9994 non-null   int64 \n",
      " 13  List Price        9994 non-null   int64 \n",
      " 14  Quantity          9994 non-null   int64 \n",
      " 15  Discount Percent  9994 non-null   int64 \n",
      "dtypes: int64(6), object(10)\n",
      "memory usage: 1.2+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "f7bc9aec-978f-4e2c-bda1-1e231a27ca03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Order Id            0\n",
      "Order Date          0\n",
      "Ship Mode           1\n",
      "Segment             0\n",
      "Country             0\n",
      "City                0\n",
      "State               0\n",
      "Postal Code         0\n",
      "Region              0\n",
      "Category            0\n",
      "Sub Category        0\n",
      "Product Id          0\n",
      "cost price          0\n",
      "List Price          0\n",
      "Quantity            0\n",
      "Discount Percent    0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#Handle Missing Values\n",
    "print(df.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "5c7fec0b-19fe-4b51-9ccd-df02a493e4a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.dropna(subset=['Ship Mode'], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5e3f728e-e836-4764-84db-f4ccd2604d7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Order Id            0\n",
      "Order Date          0\n",
      "Ship Mode           0\n",
      "Segment             0\n",
      "Country             0\n",
      "City                0\n",
      "State               0\n",
      "Postal Code         0\n",
      "Region              0\n",
      "Category            0\n",
      "Sub Category        0\n",
      "Product Id          0\n",
      "cost price          0\n",
      "List Price          0\n",
      "Quantity            0\n",
      "Discount Percent    0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(df.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3400c27b-9d60-49bd-9883-05b0c302c7ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.rename(columns={ \n",
    "    \"Order ID\":\"order_id\", \"Order Date\":\"order_date\", \"Ship Mode\":\"ship_mode\", \"Postal Code\":\"postal_code\", \"Sub Category\":\"sub_category\",\n",
    "       \"Product Id\":\"product_id\", \"cost price\":\"cost_price\", \"List Price\":\"list_price\", \"Discount Percent\":\"discount_percent\"\n",
    "}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "45ef3685-2ffb-411a-94d4-a8eb06412a25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Order Id', 'order_date', 'ship_mode', 'Segment', 'Country', 'City',\n",
      "       'State', 'postal_code', 'Region', 'Category', 'sub_category',\n",
      "       'product_id', 'cost_price', 'list_price', 'Quantity',\n",
      "       'discount_percent'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "72b8f031-a621-471d-8f74-64a962f71ef4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.rename(columns={'Order Id': 'order_id'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "55756c6a-04d1-413f-9c02-a2ad6da5b1b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['order_id', 'order_date', 'ship_mode', 'Segment', 'Country', 'City',\n",
      "       'State', 'postal_code', 'Region', 'Category', 'sub_category',\n",
      "       'product_id', 'cost_price', 'list_price', 'Quantity',\n",
      "       'discount_percent'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "fc39ca93-f673-4244-9ff1-a419abcb3bbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['sale_price'] = df['list_price'] - (df['list_price'] * df['discount_percent'] / 100)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "2e83d59a-63c9-4aef-8e5b-c227a5045ebd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     order_id  Revenue    Cost  Profit  Profit_Margin\n",
      "0           1    509.6   480.0    29.6       5.808477\n",
      "1           2   2124.3  1800.0   324.3      15.266205\n",
      "2           3     19.0    20.0    -1.0      -5.263158\n",
      "3           4   4704.0  3900.0   804.0      17.091837\n",
      "4           5     38.0    40.0    -2.0      -5.263158\n",
      "...       ...      ...     ...     ...            ...\n",
      "9989     9990     86.4    90.0    -3.6      -4.166667\n",
      "9990     9991    172.8   140.0    32.8      18.981481\n",
      "9991     9992    509.6   440.0    69.6      13.657771\n",
      "9992     9993    116.4   120.0    -3.6      -3.092784\n",
      "9993     9994    465.6   420.0    45.6       9.793814\n",
      "\n",
      "[9993 rows x 5 columns]\n"
     ]
    }
   ],
   "source": [
    "# Calculate Revenue and Cost\n",
    "df['Revenue'] = (df['list_price'] * df['Quantity']) * (1 - df['discount_percent']/100)\n",
    "df['Cost'] = df['cost_price'] * df['Quantity']\n",
    "\n",
    "# Calculate Profit\n",
    "df['Profit'] = df['Revenue'] - df['Cost']\n",
    "\n",
    "# Calculate Profit Margin\n",
    "df['Profit_Margin'] = (df['Profit'] / df['Revenue']) * 100\n",
    "\n",
    "# Display the result\n",
    "print(df[['order_id', 'Revenue', 'Cost', 'Profit', 'Profit_Margin']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "b21af6ce-2545-448a-ae59-02256d0df581",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['order_id'] = df['order_id'].astype(str)\n",
    "df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')\n",
    "df['postal_code'] = df['postal_code'].astype(str)\n",
    "df['cost_price'] = df['cost_price'].astype(float)\n",
    "df['list_price'] = df['list_price'].astype(float)\n",
    "df['Quantity'] = df['Quantity'].astype(int)\n",
    "df['discount_percent'] = df['discount_percent'].astype(float)\n",
    "df['sale_price'] = df['sale_price'].astype(float)\n",
    "df['Revenue'] = df['Revenue'].astype(float)\n",
    "df['Cost'] = df['Cost'].astype(float)\n",
    "df['Profit'] = df['Profit'].astype(float)\n",
    "df['Profit_Margin'] = df['Profit_Margin'].astype(float)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "5da9d677-e7a7-4998-8a06-3ac542c5bf9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(\"./data/cleaned_orders.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cfa0225-98d3-42b7-8f4b-cb81063617c9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
