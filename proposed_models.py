{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import pandas as pd\n",
    "df = pd.read_csv('final_dataframe1.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 179 entries, 0 to 178\n",
      "Data columns (total 23 columns):\n",
      "id              179 non-null int64\n",
      "activity        179 non-null object\n",
      "time_min        179 non-null float64\n",
      "time_max        179 non-null float64\n",
      "time_average    179 non-null float64\n",
      "x_min           179 non-null float64\n",
      "y_min           179 non-null float64\n",
      "z_min           179 non-null float64\n",
      "x_std           179 non-null float64\n",
      "y_std           179 non-null float64\n",
      "z_std           179 non-null float64\n",
      "x_var           179 non-null float64\n",
      "y_var           179 non-null float64\n",
      "z_var           179 non-null float64\n",
      "x_median        179 non-null float64\n",
      "y_median        179 non-null float64\n",
      "z_median        179 non-null float64\n",
      "x_mean          179 non-null float64\n",
      "y_mean          179 non-null float64\n",
      "z_mean          179 non-null float64\n",
      "x_max           179 non-null float64\n",
      "y_max           179 non-null float64\n",
      "z_max           179 non-null float64\n",
      "dtypes: float64(21), int64(1), object(1)\n",
      "memory usage: 32.3+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
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
       "      <th>id</th>\n",
       "      <th>activity</th>\n",
       "      <th>time_min</th>\n",
       "      <th>time_max</th>\n",
       "      <th>time_average</th>\n",
       "      <th>x_min</th>\n",
       "      <th>y_min</th>\n",
       "      <th>z_min</th>\n",
       "      <th>x_std</th>\n",
       "      <th>y_std</th>\n",
       "      <th>...</th>\n",
       "      <th>z_var</th>\n",
       "      <th>x_median</th>\n",
       "      <th>y_median</th>\n",
       "      <th>z_median</th>\n",
       "      <th>x_mean</th>\n",
       "      <th>y_mean</th>\n",
       "      <th>z_mean</th>\n",
       "      <th>x_max</th>\n",
       "      <th>y_max</th>\n",
       "      <th>z_max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Walking</td>\n",
       "      <td>4.991920e+12</td>\n",
       "      <td>5.974870e+12</td>\n",
       "      <td>5.472666e+12</td>\n",
       "      <td>-19.61</td>\n",
       "      <td>-5.79</td>\n",
       "      <td>-15.09</td>\n",
       "      <td>6.967989</td>\n",
       "      <td>5.396160</td>\n",
       "      <td>...</td>\n",
       "      <td>10.373247</td>\n",
       "      <td>-1.23</td>\n",
       "      <td>9.62</td>\n",
       "      <td>-0.72</td>\n",
       "      <td>-1.000041</td>\n",
       "      <td>9.455536</td>\n",
       "      <td>-0.343607</td>\n",
       "      <td>19.57</td>\n",
       "      <td>19.57</td>\n",
       "      <td>13.44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Jogging</td>\n",
       "      <td>5.374660e+12</td>\n",
       "      <td>6.298490e+12</td>\n",
       "      <td>5.854316e+12</td>\n",
       "      <td>-19.61</td>\n",
       "      <td>-19.61</td>\n",
       "      <td>-17.20</td>\n",
       "      <td>10.706282</td>\n",
       "      <td>9.483499</td>\n",
       "      <td>...</td>\n",
       "      <td>31.966332</td>\n",
       "      <td>-0.04</td>\n",
       "      <td>0.42</td>\n",
       "      <td>0.57</td>\n",
       "      <td>-0.208456</td>\n",
       "      <td>0.197931</td>\n",
       "      <td>1.164557</td>\n",
       "      <td>19.57</td>\n",
       "      <td>19.57</td>\n",
       "      <td>19.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Upstairs</td>\n",
       "      <td>6.489310e+12</td>\n",
       "      <td>6.848770e+12</td>\n",
       "      <td>6.668160e+12</td>\n",
       "      <td>-19.61</td>\n",
       "      <td>-13.95</td>\n",
       "      <td>-16.44</td>\n",
       "      <td>7.779192</td>\n",
       "      <td>6.492359</td>\n",
       "      <td>...</td>\n",
       "      <td>22.574183</td>\n",
       "      <td>-6.70</td>\n",
       "      <td>5.09</td>\n",
       "      <td>0.15</td>\n",
       "      <td>-6.349433</td>\n",
       "      <td>5.332679</td>\n",
       "      <td>0.633660</td>\n",
       "      <td>16.55</td>\n",
       "      <td>19.57</td>\n",
       "      <td>18.58</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>Downstairs</td>\n",
       "      <td>6.552940e+12</td>\n",
       "      <td>6.895550e+12</td>\n",
       "      <td>6.726542e+12</td>\n",
       "      <td>-19.61</td>\n",
       "      <td>-5.01</td>\n",
       "      <td>-10.15</td>\n",
       "      <td>8.061251</td>\n",
       "      <td>4.761467</td>\n",
       "      <td>...</td>\n",
       "      <td>15.828829</td>\n",
       "      <td>-0.84</td>\n",
       "      <td>8.54</td>\n",
       "      <td>-0.11</td>\n",
       "      <td>-1.033366</td>\n",
       "      <td>8.542870</td>\n",
       "      <td>0.575641</td>\n",
       "      <td>19.57</td>\n",
       "      <td>19.57</td>\n",
       "      <td>17.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>Walking</td>\n",
       "      <td>7.981270e+12</td>\n",
       "      <td>1.001250e+13</td>\n",
       "      <td>9.028226e+12</td>\n",
       "      <td>-19.50</td>\n",
       "      <td>-3.21</td>\n",
       "      <td>-17.27</td>\n",
       "      <td>3.151260</td>\n",
       "      <td>3.480465</td>\n",
       "      <td>...</td>\n",
       "      <td>11.788414</td>\n",
       "      <td>-4.21</td>\n",
       "      <td>8.77</td>\n",
       "      <td>-0.50</td>\n",
       "      <td>-4.281787</td>\n",
       "      <td>8.764060</td>\n",
       "      <td>-0.571448</td>\n",
       "      <td>10.92</td>\n",
       "      <td>19.57</td>\n",
       "      <td>11.14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   id    activity      time_min      time_max  time_average  x_min  y_min  \\\n",
       "0   1     Walking  4.991920e+12  5.974870e+12  5.472666e+12 -19.61  -5.79   \n",
       "1   1     Jogging  5.374660e+12  6.298490e+12  5.854316e+12 -19.61 -19.61   \n",
       "2   1    Upstairs  6.489310e+12  6.848770e+12  6.668160e+12 -19.61 -13.95   \n",
       "3   1  Downstairs  6.552940e+12  6.895550e+12  6.726542e+12 -19.61  -5.01   \n",
       "4   2     Walking  7.981270e+12  1.001250e+13  9.028226e+12 -19.50  -3.21   \n",
       "\n",
       "   z_min      x_std     y_std  ...      z_var  x_median  y_median  z_median  \\\n",
       "0 -15.09   6.967989  5.396160  ...  10.373247     -1.23      9.62     -0.72   \n",
       "1 -17.20  10.706282  9.483499  ...  31.966332     -0.04      0.42      0.57   \n",
       "2 -16.44   7.779192  6.492359  ...  22.574183     -6.70      5.09      0.15   \n",
       "3 -10.15   8.061251  4.761467  ...  15.828829     -0.84      8.54     -0.11   \n",
       "4 -17.27   3.151260  3.480465  ...  11.788414     -4.21      8.77     -0.50   \n",
       "\n",
       "     x_mean    y_mean    z_mean  x_max  y_max  z_max  \n",
       "0 -1.000041  9.455536 -0.343607  19.57  19.57  13.44  \n",
       "1 -0.208456  0.197931  1.164557  19.57  19.57  19.00  \n",
       "2 -6.349433  5.332679  0.633660  16.55  19.57  18.58  \n",
       "3 -1.033366  8.542870  0.575641  19.57  19.57  17.05  \n",
       "4 -4.281787  8.764060 -0.571448  10.92  19.57  11.14  \n",
       "\n",
       "[5 rows x 23 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      0\n",
      "1      1\n",
      "2      3\n",
      "3      4\n",
      "4      0\n",
      "      ..\n",
      "174    1\n",
      "175    2\n",
      "176    3\n",
      "177    4\n",
      "178    5\n",
      "Name: activity, Length: 179, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "label = df[\"activity\"].map({\"Walking\":0,\"Jogging\":1, \"Sitting\":2,\"Upstairs\":3,\"Downstairs\":4,\"Standing\":5})\n",
    "print(label)\n",
    "df[\"label\"]=label\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      1\n",
      "1      2\n",
      "2      1\n",
      "3      1\n",
      "4      1\n",
      "      ..\n",
      "174    2\n",
      "175    3\n",
      "176    1\n",
      "177    1\n",
      "178    3\n",
      "Name: activity, Length: 179, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "final_label = df[\"activity\"].map({\"Walking\":1,\"Jogging\":2, \"Sitting\":3,\"Upstairs\":1,\"Downstairs\":1,\"Standing\":3})\n",
    "print(final_label)\n",
    "df[\"final_label\"]=final_label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(r'final_dataframe_threeclass.csv',index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   id    activity      time_min      time_max  time_average  x_min  y_min  \\\n",
      "0   1     Walking  4.991920e+12  5.974870e+12  5.472666e+12 -19.61  -5.79   \n",
      "1   1     Jogging  5.374660e+12  6.298490e+12  5.854316e+12 -19.61 -19.61   \n",
      "2   1    Upstairs  6.489310e+12  6.848770e+12  6.668160e+12 -19.61 -13.95   \n",
      "3   1  Downstairs  6.552940e+12  6.895550e+12  6.726542e+12 -19.61  -5.01   \n",
      "4   2     Walking  7.981270e+12  1.001250e+13  9.028226e+12 -19.50  -3.21   \n",
      "\n",
      "   z_min      x_std     y_std  ...  y_median  z_median    x_mean    y_mean  \\\n",
      "0 -15.09   6.967989  5.396160  ...      9.62     -0.72 -1.000041  9.455536   \n",
      "1 -17.20  10.706282  9.483499  ...      0.42      0.57 -0.208456  0.197931   \n",
      "2 -16.44   7.779192  6.492359  ...      5.09      0.15 -6.349433  5.332679   \n",
      "3 -10.15   8.061251  4.761467  ...      8.54     -0.11 -1.033366  8.542870   \n",
      "4 -17.27   3.151260  3.480465  ...      8.77     -0.50 -4.281787  8.764060   \n",
      "\n",
      "     z_mean  x_max  y_max  z_max  label  final_label  \n",
      "0 -0.343607  19.57  19.57  13.44      0            1  \n",
      "1  1.164557  19.57  19.57  19.00      1            2  \n",
      "2  0.633660  16.55  19.57  18.58      3            1  \n",
      "3  0.575641  19.57  19.57  17.05      4            1  \n",
      "4 -0.571448  10.92  19.57  11.14      0            1  \n",
      "\n",
      "[5 rows x 25 columns]\n"
     ]
    }
   ],
   "source": [
    "print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df.iloc[0:179:, 2:23].values\n",
    "y = df.iloc[0:179, 24].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "seed = 1\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = seed)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import datasets\n",
    "from sklearn.model_selection import cross_val_score\n",
    "from sklearn import svm\n",
    "from sklearn.metrics import confusion_matrix\n",
    "import itertools\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn import model_selection\n",
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',\n",
       "                       max_depth=None, max_features='auto', max_leaf_nodes=None,\n",
       "                       min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "                       min_samples_leaf=1, min_samples_split=2,\n",
       "                       min_weight_fraction_leaf=0.0, n_estimators=10,\n",
       "                       n_jobs=None, oob_score=False, random_state=0, verbose=0,\n",
       "                       warm_start=False)"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)\n",
    "classifier.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 88.89%\n"
     ]
    }
   ],
   "source": [
    "y_pred = classifier.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "# Making the Confusion Matrix\n",
    "from sklearn.metrics import confusion_matrix\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(\"Accuracy: %.2f%%\" % (accuracy * 100.0))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9664141414141414\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#adaboost.\n",
    "clf = RandomForestClassifier(n_estimators=50,n_jobs=-1)\n",
    "classifier = AdaBoostClassifier(base_estimator=clf,n_estimators=clf.n_estimators)\n",
    "clf = classifier.fit(X_train, y_train)\n",
    "from sklearn.model_selection import cross_val_score\n",
    "accuracies = cross_val_score(estimator = clf, X = X, y = y, cv = 4)\n",
    "print(accuracies.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
