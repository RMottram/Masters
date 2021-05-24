{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os, sys\n",
    "\n",
    "pd.set_option('display.max_columns', None)\n",
    "pd.options.display.float_format = '{:.5f}'.format\n",
    "np.set_printoptions(threshold=sys.maxsize)\n",
    "np.set_printoptions(precision = 5, suppress = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "## splits, encodes and equalizes the data\n",
    "\n",
    "def split_dataset(dataset = str(sys.argv[0]), train_split = float(sys.argv[1])):\n",
    "    df = pd.read_csv(dataset)\n",
    "    master_copy = df.copy()\n",
    "    \n",
    "    ## removes these features to level out dataset\n",
    "    df = df.query(\"service != 'aol'\")\n",
    "    df = df.query(\"service != 'harvest'\")\n",
    "    df = df.query(\"service != 'http_2784'\")\n",
    "    df = df.query(\"service != 'http_8001'\")\n",
    "    df = df.query(\"service != 'red_i'\")\n",
    "    df = df.query(\"service != 'urh_i'\")\n",
    "    df = df.query(\"service != 'printer'\")\n",
    "    df = df.query(\"service != 'rje'\")\n",
    "    df = df.query(\"service != 'printer'\")\n",
    "    df = df.query(\"service != 'rje'\")\n",
    "    \n",
    "    ## changes all the attack types to simply 'attack'\n",
    "    df.loc[df.attack_type != 'normal', 'attack_type'] = 'attack'\n",
    "    \n",
    "    ## OHE protocol, service and flag features\n",
    "    proto_ohe = pd.get_dummies(df['protocol_type'])\n",
    "    service_ohe = pd.get_dummies(df['service'])\n",
    "    flag_ohe = pd.get_dummies(df['flag'])\n",
    "    \n",
    "    df = df.drop(['protocol_type', 'service', 'flag'], axis = 1)\n",
    "    df = pd.concat([df, proto_ohe, service_ohe, flag_ohe], axis = 1)\n",
    "    \n",
    "    ## makes sure there are no NaNs\n",
    "    for column in df:\n",
    "        if df[column].isna().any():\n",
    "            df[column] = float(0)\n",
    "    \n",
    "    ## drop the 'attack_type' column so it does not get normalises\n",
    "    df_labels = df['attack_type']\n",
    "    df = df.drop(['attack_type'], axis = 1)\n",
    "    df = 255 * df / df.max(numeric_only = True)\n",
    "    \n",
    "    df['attack_type'] = df_labels\n",
    "    \n",
    "    train = df.sample(frac = train_split)\n",
    "    test = df.drop(train.index)\n",
    "    \n",
    "    return train, test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "# train, test = split_dataset(dataset = 'combined_dataset.csv', train_split = 0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/Users/ryan/NSL CNN/2d-cnn\n"
     ]
    }
   ],
   "source": [
    "# !pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "# os.chdir('datasets')"
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
      "/Users/ryan/NSL CNN/2d-cnn/datasets\n"
     ]
    }
   ],
   "source": [
    "# !pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "# train.to_csv('train_5050.csv', index = 0)\n",
    "# test.to_csv('test_5050.csv', index = 0)"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
