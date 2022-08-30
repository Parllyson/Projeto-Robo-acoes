{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dc6e62a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fb3eef96",
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
       "      <th>Código</th>\n",
       "      <th>Ação</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ABEV3</td>\n",
       "      <td>AMBEV S/A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AZUL4</td>\n",
       "      <td>AZUL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>B3SA3</td>\n",
       "      <td>B3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>BBAS3</td>\n",
       "      <td>BRASIL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>BBDC3</td>\n",
       "      <td>BRADESCO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>65</th>\n",
       "      <td>USIM5</td>\n",
       "      <td>USIMINAS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>66</th>\n",
       "      <td>VALE3</td>\n",
       "      <td>VALE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>67</th>\n",
       "      <td>VIVT4</td>\n",
       "      <td>TELEF BRASIL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>68</th>\n",
       "      <td>WEGE3</td>\n",
       "      <td>WEG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69</th>\n",
       "      <td>YDUQ3</td>\n",
       "      <td>YDUQS PART</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>70 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Código          Ação\n",
       "0   ABEV3     AMBEV S/A\n",
       "1   AZUL4          AZUL\n",
       "2   B3SA3            B3\n",
       "3   BBAS3        BRASIL\n",
       "4   BBDC3      BRADESCO\n",
       "..    ...           ...\n",
       "65  USIM5      USIMINAS\n",
       "66  VALE3          VALE\n",
       "67  VIVT4  TELEF BRASIL\n",
       "68  WEGE3           WEG\n",
       "69  YDUQ3    YDUQS PART\n",
       "\n",
       "[70 rows x 2 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "### Ler arquivo Excel.\n",
    "acoes_ibov = pd.read_excel(\"IBOV.xlsx\")\n",
    "\n",
    "display(acoes_ibov)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fbe3d831",
   "metadata": {
    "scrolled": true
   },
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
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: []\n",
       "Index: []"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação ABEV3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação AZUL4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação B3SA3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação BBAS3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação BBDC3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação BBDC4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação BBSE3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação BPAC11\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação BRAP4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação BRFS3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação BRKM5\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação BRML3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação CCRO3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação CIEL3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação CMIG4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação COGN3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação CRFB3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação CSAN3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação CSNA3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação CVCB3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação CYRE3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação ECOR3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação EGIE3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação ELET3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação ELET6\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação EMBR3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação ENBR3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação EQTL3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação FLRY3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação GGBR4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação GNDI3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação GOAU4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação GOLL4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação HAPV3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação HGTX3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação HYPE3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação IGTA3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação IRBR3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação ITSA4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação ITUB4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação JBSS3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação KLBN11\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação LAME4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação LREN3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação MGLU3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação MRFG3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação MRVE3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação MULT3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação NTCO3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação PCAR3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação PETR3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação PETR4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação QUAL3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação RADL3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação RAIL3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação RENT3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação SANB11\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação SBSP3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação SMLS3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação SULA11\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação SUZB3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação TAEE11\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação TIMP3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação TOTS3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação UGPA3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação USIM5\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação VALE3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação VIVT4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação WEGE3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou acessando informações da Ação YDUQ3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alexandre\\AppData\\Local\\Temp\\ipykernel_8236\\2706403951.py:50: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
      "  consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n"
     ]
    },
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
       "      <th>?Papel</th>\n",
       "      <th>?Tipo</th>\n",
       "      <th>?Empresa</th>\n",
       "      <th>?Setor</th>\n",
       "      <th>?Subsetor</th>\n",
       "      <th>?Cotação</th>\n",
       "      <th>?Data últ cot</th>\n",
       "      <th>?Min 52 sem</th>\n",
       "      <th>?Max 52 sem</th>\n",
       "      <th>?Vol $ méd (2m)</th>\n",
       "      <th>?Valor de mercado</th>\n",
       "      <th>?Valor da firma</th>\n",
       "      <th>?Últ balanço processado</th>\n",
       "      <th>?Nro. Ações</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ABEV3</td>\n",
       "      <td>ON</td>\n",
       "      <td>AMBEV S/A ON</td>\n",
       "      <td>Bebidas</td>\n",
       "      <td>Cervejas e Refrigerantes</td>\n",
       "      <td>16.00</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>13.03</td>\n",
       "      <td>17.31</td>\n",
       "      <td>356860000</td>\n",
       "      <td>252003000000</td>\n",
       "      <td>239535000000</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>15750200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AZUL4</td>\n",
       "      <td>PN</td>\n",
       "      <td>AZUL PN</td>\n",
       "      <td>Transporte</td>\n",
       "      <td>Transporte Aéreo</td>\n",
       "      <td>17.31</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>11.07</td>\n",
       "      <td>39.74</td>\n",
       "      <td>143064000</td>\n",
       "      <td>6023860000</td>\n",
       "      <td>27165200000</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>347999000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B3SA3</td>\n",
       "      <td>ON</td>\n",
       "      <td>B3 ON</td>\n",
       "      <td>Serviços Financeiros Diversos</td>\n",
       "      <td>Serviços Financeiros Diversos</td>\n",
       "      <td>12.85</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>10.03</td>\n",
       "      <td>15.96</td>\n",
       "      <td>408452000</td>\n",
       "      <td>78372200000</td>\n",
       "      <td>75895000000</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>6099000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>BBAS3</td>\n",
       "      <td>ON</td>\n",
       "      <td>BANCO DO BRASIL S.A. ON</td>\n",
       "      <td>Intermediários Financeiros</td>\n",
       "      <td>Bancos</td>\n",
       "      <td>41.82</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>26.24</td>\n",
       "      <td>44.10</td>\n",
       "      <td>532924000</td>\n",
       "      <td>119832000000</td>\n",
       "      <td>-</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>2865420000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>BBDC3</td>\n",
       "      <td>ON N1</td>\n",
       "      <td>BANCO BRADESCO S.A. ON N1</td>\n",
       "      <td>Intermediários Financeiros</td>\n",
       "      <td>Bancos</td>\n",
       "      <td>16.43</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>13.62</td>\n",
       "      <td>17.72</td>\n",
       "      <td>94470100</td>\n",
       "      <td>175119000000</td>\n",
       "      <td>-</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>10658500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>USIM5</td>\n",
       "      <td>PNA N1</td>\n",
       "      <td>USIMINAS PNA N1</td>\n",
       "      <td>Siderurgia e Metalurgia</td>\n",
       "      <td>Siderurgia</td>\n",
       "      <td>9.19</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>8.05</td>\n",
       "      <td>16.51</td>\n",
       "      <td>148494000</td>\n",
       "      <td>11515800000</td>\n",
       "      <td>11966700000</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>1253080000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>VALE3</td>\n",
       "      <td>ON NM</td>\n",
       "      <td>VALE ON NM</td>\n",
       "      <td>Mineração</td>\n",
       "      <td>Minerais Metálicos</td>\n",
       "      <td>67.72</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>57.25</td>\n",
       "      <td>96.51</td>\n",
       "      <td>2131880000</td>\n",
       "      <td>323626000000</td>\n",
       "      <td>351782000000</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>4778890000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>VIVT4</td>\n",
       "      <td>PN</td>\n",
       "      <td>TELEF BRASIL PN</td>\n",
       "      <td>Telecomunicações</td>\n",
       "      <td>Telecomunicações</td>\n",
       "      <td>45.34</td>\n",
       "      <td>20/11/2020</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>76032400000</td>\n",
       "      <td>89282600000</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>1676940000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>WEGE3</td>\n",
       "      <td>ON N1</td>\n",
       "      <td>WEG SA ON N1</td>\n",
       "      <td>Máquinas e Equipamentos</td>\n",
       "      <td>Motores, Compressores e Outros</td>\n",
       "      <td>30.84</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>22.68</td>\n",
       "      <td>40.69</td>\n",
       "      <td>223073000</td>\n",
       "      <td>129445000000</td>\n",
       "      <td>129227000000</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>4197320000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>YDUQ3</td>\n",
       "      <td>ON</td>\n",
       "      <td>YDUQS PART ON</td>\n",
       "      <td>Diversos</td>\n",
       "      <td>Serviços Educacionais</td>\n",
       "      <td>12.55</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>12.42</td>\n",
       "      <td>27.76</td>\n",
       "      <td>53325400</td>\n",
       "      <td>3879070000</td>\n",
       "      <td>8048170000</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>309089000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>70 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "0  ?Papel   ?Tipo                   ?Empresa                         ?Setor  \\\n",
       "1   ABEV3      ON               AMBEV S/A ON                        Bebidas   \n",
       "1   AZUL4      PN                    AZUL PN                     Transporte   \n",
       "1   B3SA3      ON                      B3 ON  Serviços Financeiros Diversos   \n",
       "1   BBAS3      ON    BANCO DO BRASIL S.A. ON     Intermediários Financeiros   \n",
       "1   BBDC3   ON N1  BANCO BRADESCO S.A. ON N1     Intermediários Financeiros   \n",
       "..    ...     ...                        ...                            ...   \n",
       "1   USIM5  PNA N1            USIMINAS PNA N1        Siderurgia e Metalurgia   \n",
       "1   VALE3   ON NM                 VALE ON NM                      Mineração   \n",
       "1   VIVT4      PN            TELEF BRASIL PN               Telecomunicações   \n",
       "1   WEGE3   ON N1               WEG SA ON N1        Máquinas e Equipamentos   \n",
       "1   YDUQ3      ON              YDUQS PART ON                       Diversos   \n",
       "\n",
       "0                        ?Subsetor ?Cotação ?Data últ cot ?Min 52 sem  \\\n",
       "1         Cervejas e Refrigerantes    16.00    18/08/2022       13.03   \n",
       "1                 Transporte Aéreo    17.31    18/08/2022       11.07   \n",
       "1    Serviços Financeiros Diversos    12.85    18/08/2022       10.03   \n",
       "1                           Bancos    41.82    18/08/2022       26.24   \n",
       "1                           Bancos    16.43    18/08/2022       13.62   \n",
       "..                             ...      ...           ...         ...   \n",
       "1                       Siderurgia     9.19    18/08/2022        8.05   \n",
       "1               Minerais Metálicos    67.72    18/08/2022       57.25   \n",
       "1                 Telecomunicações    45.34    20/11/2020        0.00   \n",
       "1   Motores, Compressores e Outros    30.84    18/08/2022       22.68   \n",
       "1            Serviços Educacionais    12.55    18/08/2022       12.42   \n",
       "\n",
       "0  ?Max 52 sem ?Vol $ méd (2m) ?Valor de mercado ?Valor da firma  \\\n",
       "1        17.31       356860000      252003000000    239535000000   \n",
       "1        39.74       143064000        6023860000     27165200000   \n",
       "1        15.96       408452000       78372200000     75895000000   \n",
       "1        44.10       532924000      119832000000               -   \n",
       "1        17.72        94470100      175119000000               -   \n",
       "..         ...             ...               ...             ...   \n",
       "1        16.51       148494000       11515800000     11966700000   \n",
       "1        96.51      2131880000      323626000000    351782000000   \n",
       "1         0.00               0       76032400000     89282600000   \n",
       "1        40.69       223073000      129445000000    129227000000   \n",
       "1        27.76        53325400        3879070000      8048170000   \n",
       "\n",
       "0  ?Últ balanço processado  ?Nro. Ações  \n",
       "1               30/06/2022  15750200000  \n",
       "1               30/06/2022    347999000  \n",
       "1               30/06/2022   6099000000  \n",
       "1               30/06/2022   2865420000  \n",
       "1               30/06/2022  10658500000  \n",
       "..                     ...          ...  \n",
       "1               30/06/2022   1253080000  \n",
       "1               30/06/2022   4778890000  \n",
       "1               30/06/2022   1676940000  \n",
       "1               30/06/2022   4197320000  \n",
       "1               30/06/2022    309089000  \n",
       "\n",
       "[70 rows x 14 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "consolidacao_acoes = pd.DataFrame()\n",
    "\n",
    "display(consolidacao_acoes)\n",
    "\n",
    "for codigo_acao in acoes_ibov[\"Código\"]:\n",
    "    print(f\"Estou acessando informações da Ação\", codigo_acao)\n",
    "    # URL que desejo coletar os dados.\n",
    "\n",
    "    url = 'https://www.fundamentus.com.br/detalhes.php?papel=' + codigo_acao\n",
    "\n",
    "    # Informações para fingir ser um navegador, para a página não bloquear o acesso.\n",
    "\n",
    "    header = {\n",
    "        \"User-Agent\": \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36\",\n",
    "      \"X-Requested-With\": \"XMLHttpRequest\"\n",
    "    }\n",
    "\n",
    "    # Juntando os dados da requests\n",
    "    r = requests.get(url, headers=header)\n",
    "    # Agora usamos a fundão do pandas pd.read_html\n",
    "\n",
    "    dfs = pd.read_html(r.text, thousands='.', decimal=',')\n",
    "\n",
    "\n",
    "    # Transpose = Colocar o titulo/menu em seu respectivo lugar.\n",
    "    dfs[0] = dfs[0].transpose()\n",
    "    dfs[1] = dfs[1].transpose()\n",
    "\n",
    "\n",
    "    # Localizar as linhas necessárias e separar as tabelas para tratamento de dados.\n",
    "    informacoes_1t1 = dfs[0].iloc[:2, :]\n",
    "    informacoes_2t1 = dfs[0].iloc[2:, :]\n",
    "    informacoes_1t2 = dfs[1].iloc[:2, :]\n",
    "    informacoes_2t2 = dfs[1].iloc[2:, :]\n",
    "\n",
    "\n",
    "    # Precisamos agora resetar o index das linhas.\n",
    "    informacoes_2t1 = informacoes_2t1.reset_index(drop=True)\n",
    "    informacoes_2t2 = informacoes_2t2.reset_index(drop=True)\n",
    "\n",
    "\n",
    "    # Agora precisamos concatenar as tabelas.\n",
    "    dfs = pd.concat([informacoes_1t1, informacoes_2t1, informacoes_1t2, informacoes_2t2], axis=1, join='inner')\n",
    "\n",
    "    #passar a linha para o cabeçalho (que é o correto)\n",
    "\n",
    "    dfs.columns = dfs.iloc[0]\n",
    "    dfs = dfs.drop(0)\n",
    "\n",
    "    consolidacao_acoes = consolidacao_acoes.append(dfs, sort=False)\n",
    "    \n",
    "\n",
    "display(consolidacao_acoes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8f5958c3",
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
       "      <th>Papel</th>\n",
       "      <th>Tipo</th>\n",
       "      <th>Empresa</th>\n",
       "      <th>Setor</th>\n",
       "      <th>Subsetor</th>\n",
       "      <th>Cotação</th>\n",
       "      <th>Data últ cot</th>\n",
       "      <th>Min 52 sem</th>\n",
       "      <th>Max 52 sem</th>\n",
       "      <th>Vol $ méd (2m)</th>\n",
       "      <th>Valor de mercado</th>\n",
       "      <th>Valor da firma</th>\n",
       "      <th>Últ balanço processado</th>\n",
       "      <th>Nro. Ações</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ABEV3</td>\n",
       "      <td>ON</td>\n",
       "      <td>AMBEV S/A ON</td>\n",
       "      <td>Bebidas</td>\n",
       "      <td>Cervejas e Refrigerantes</td>\n",
       "      <td>16.00</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>13.03</td>\n",
       "      <td>17.31</td>\n",
       "      <td>356860000</td>\n",
       "      <td>252003000000</td>\n",
       "      <td>2.395350e+11</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>15750200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AZUL4</td>\n",
       "      <td>PN</td>\n",
       "      <td>AZUL PN</td>\n",
       "      <td>Transporte</td>\n",
       "      <td>Transporte Aéreo</td>\n",
       "      <td>17.31</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>11.07</td>\n",
       "      <td>39.74</td>\n",
       "      <td>143064000</td>\n",
       "      <td>6023860000</td>\n",
       "      <td>2.716520e+10</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>347999000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>B3SA3</td>\n",
       "      <td>ON</td>\n",
       "      <td>B3 ON</td>\n",
       "      <td>Serviços Financeiros Diversos</td>\n",
       "      <td>Serviços Financeiros Diversos</td>\n",
       "      <td>12.85</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>10.03</td>\n",
       "      <td>15.96</td>\n",
       "      <td>408452000</td>\n",
       "      <td>78372200000</td>\n",
       "      <td>7.589500e+10</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>6099000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>BBAS3</td>\n",
       "      <td>ON</td>\n",
       "      <td>BANCO DO BRASIL S.A. ON</td>\n",
       "      <td>Intermediários Financeiros</td>\n",
       "      <td>Bancos</td>\n",
       "      <td>41.82</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>26.24</td>\n",
       "      <td>44.10</td>\n",
       "      <td>532924000</td>\n",
       "      <td>119832000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>2865420000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>BBDC3</td>\n",
       "      <td>ON N1</td>\n",
       "      <td>BANCO BRADESCO S.A. ON N1</td>\n",
       "      <td>Intermediários Financeiros</td>\n",
       "      <td>Bancos</td>\n",
       "      <td>16.43</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>13.62</td>\n",
       "      <td>17.72</td>\n",
       "      <td>94470100</td>\n",
       "      <td>175119000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>10658500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>65</th>\n",
       "      <td>USIM5</td>\n",
       "      <td>PNA N1</td>\n",
       "      <td>USIMINAS PNA N1</td>\n",
       "      <td>Siderurgia e Metalurgia</td>\n",
       "      <td>Siderurgia</td>\n",
       "      <td>9.19</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>8.05</td>\n",
       "      <td>16.51</td>\n",
       "      <td>148494000</td>\n",
       "      <td>11515800000</td>\n",
       "      <td>1.196670e+10</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>1253080000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>66</th>\n",
       "      <td>VALE3</td>\n",
       "      <td>ON NM</td>\n",
       "      <td>VALE ON NM</td>\n",
       "      <td>Mineração</td>\n",
       "      <td>Minerais Metálicos</td>\n",
       "      <td>67.72</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>57.25</td>\n",
       "      <td>96.51</td>\n",
       "      <td>2131880000</td>\n",
       "      <td>323626000000</td>\n",
       "      <td>3.517820e+11</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>4778890000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>67</th>\n",
       "      <td>VIVT4</td>\n",
       "      <td>PN</td>\n",
       "      <td>TELEF BRASIL PN</td>\n",
       "      <td>Telecomunicações</td>\n",
       "      <td>Telecomunicações</td>\n",
       "      <td>45.34</td>\n",
       "      <td>20/11/2020</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>76032400000</td>\n",
       "      <td>8.928260e+10</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>1676940000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>68</th>\n",
       "      <td>WEGE3</td>\n",
       "      <td>ON N1</td>\n",
       "      <td>WEG SA ON N1</td>\n",
       "      <td>Máquinas e Equipamentos</td>\n",
       "      <td>Motores, Compressores e Outros</td>\n",
       "      <td>30.84</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>22.68</td>\n",
       "      <td>40.69</td>\n",
       "      <td>223073000</td>\n",
       "      <td>129445000000</td>\n",
       "      <td>1.292270e+11</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>4197320000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69</th>\n",
       "      <td>YDUQ3</td>\n",
       "      <td>ON</td>\n",
       "      <td>YDUQS PART ON</td>\n",
       "      <td>Diversos</td>\n",
       "      <td>Serviços Educacionais</td>\n",
       "      <td>12.55</td>\n",
       "      <td>18/08/2022</td>\n",
       "      <td>12.42</td>\n",
       "      <td>27.76</td>\n",
       "      <td>53325400</td>\n",
       "      <td>3879070000</td>\n",
       "      <td>8.048170e+09</td>\n",
       "      <td>30/06/2022</td>\n",
       "      <td>309089000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>70 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Papel    Tipo                    Empresa                          Setor  \\\n",
       "0   ABEV3      ON               AMBEV S/A ON                        Bebidas   \n",
       "1   AZUL4      PN                    AZUL PN                     Transporte   \n",
       "2   B3SA3      ON                      B3 ON  Serviços Financeiros Diversos   \n",
       "3   BBAS3      ON    BANCO DO BRASIL S.A. ON     Intermediários Financeiros   \n",
       "4   BBDC3   ON N1  BANCO BRADESCO S.A. ON N1     Intermediários Financeiros   \n",
       "..    ...     ...                        ...                            ...   \n",
       "65  USIM5  PNA N1            USIMINAS PNA N1        Siderurgia e Metalurgia   \n",
       "66  VALE3   ON NM                 VALE ON NM                      Mineração   \n",
       "67  VIVT4      PN            TELEF BRASIL PN               Telecomunicações   \n",
       "68  WEGE3   ON N1               WEG SA ON N1        Máquinas e Equipamentos   \n",
       "69  YDUQ3      ON              YDUQS PART ON                       Diversos   \n",
       "\n",
       "                          Subsetor Cotação Data últ cot Min 52 sem Max 52 sem  \\\n",
       "0         Cervejas e Refrigerantes   16.00   18/08/2022      13.03      17.31   \n",
       "1                 Transporte Aéreo   17.31   18/08/2022      11.07      39.74   \n",
       "2    Serviços Financeiros Diversos   12.85   18/08/2022      10.03      15.96   \n",
       "3                           Bancos   41.82   18/08/2022      26.24      44.10   \n",
       "4                           Bancos   16.43   18/08/2022      13.62      17.72   \n",
       "..                             ...     ...          ...        ...        ...   \n",
       "65                      Siderurgia    9.19   18/08/2022       8.05      16.51   \n",
       "66              Minerais Metálicos   67.72   18/08/2022      57.25      96.51   \n",
       "67                Telecomunicações   45.34   20/11/2020       0.00       0.00   \n",
       "68  Motores, Compressores e Outros   30.84   18/08/2022      22.68      40.69   \n",
       "69           Serviços Educacionais   12.55   18/08/2022      12.42      27.76   \n",
       "\n",
       "    Vol $ méd (2m)  Valor de mercado  Valor da firma Últ balanço processado  \\\n",
       "0        356860000      252003000000    2.395350e+11             30/06/2022   \n",
       "1        143064000        6023860000    2.716520e+10             30/06/2022   \n",
       "2        408452000       78372200000    7.589500e+10             30/06/2022   \n",
       "3        532924000      119832000000             NaN             30/06/2022   \n",
       "4         94470100      175119000000             NaN             30/06/2022   \n",
       "..             ...               ...             ...                    ...   \n",
       "65       148494000       11515800000    1.196670e+10             30/06/2022   \n",
       "66      2131880000      323626000000    3.517820e+11             30/06/2022   \n",
       "67               0       76032400000    8.928260e+10             30/06/2022   \n",
       "68       223073000      129445000000    1.292270e+11             30/06/2022   \n",
       "69        53325400        3879070000    8.048170e+09             30/06/2022   \n",
       "\n",
       "     Nro. Ações  \n",
       "0   15750200000  \n",
       "1     347999000  \n",
       "2    6099000000  \n",
       "3    2865420000  \n",
       "4   10658500000  \n",
       "..          ...  \n",
       "65   1253080000  \n",
       "66   4778890000  \n",
       "67   1676940000  \n",
       "68   4197320000  \n",
       "69    309089000  \n",
       "\n",
       "[70 rows x 14 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "consolidacao_acoes = consolidacao_acoes.reset_index(drop=True)\n",
    "\n",
    "novo_cabecalho = [coluna.replace(\"?\", \"\") for coluna in consolidacao_acoes.columns]\n",
    "\n",
    "consolidacao_acoes.columns = novo_cabecalho\n",
    "\n",
    "#correção de datas apenas.\n",
    "consolidacao_acoes['Data últ cot'] = pd.to_datetime(consolidacao_acoes['Data últ cot'], errors='ignore', format='%d/%m/%y')\n",
    "consolidacao_acoes['Últ balanço processado'] = pd.to_datetime(consolidacao_acoes['Últ balanço processado'], errors='ignore', format='%d/%m/%y') \n",
    "\n",
    "# Corrigir números\n",
    "\n",
    "consolidacao_acoes['Vol $ méd (2m)'] = pd.to_numeric(consolidacao_acoes['Vol $ méd (2m)'], errors='coerce')\n",
    "consolidacao_acoes['Valor de mercado'] = pd.to_numeric(consolidacao_acoes['Valor de mercado'], errors='coerce')\n",
    "consolidacao_acoes['Valor da firma'] = pd.to_numeric(consolidacao_acoes['Valor da firma'], errors='coerce')\n",
    "consolidacao_acoes['Nro. Ações'] = pd.to_numeric(consolidacao_acoes['Nro. Ações'], errors='coerce')\n",
    "\n",
    "\n",
    "display(consolidacao_acoes)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
