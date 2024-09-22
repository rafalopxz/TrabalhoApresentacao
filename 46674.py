{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOlLv06UPYhrTUHlL7pN3WK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rafalopxz/TrabalhoApresentacao/blob/main/46674.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uML15vre5RQf",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 408
        },
        "outputId": "95f4e03f-ad19-42d2-94d8-f77381123548"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "JSONDecodeError",
          "evalue": "Expecting value: line 1 column 1 (char 0)",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mJSONDecodeError\u001b[0m                           Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/requests/models.py\u001b[0m in \u001b[0;36mjson\u001b[0;34m(self, **kwargs)\u001b[0m\n\u001b[1;32m    962\u001b[0m                 \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 963\u001b[0;31m                     \u001b[0;32mreturn\u001b[0m \u001b[0mcomplexjson\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcontent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mencoding\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    964\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mUnicodeDecodeError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/json/__init__.py\u001b[0m in \u001b[0;36mloads\u001b[0;34m(s, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)\u001b[0m\n\u001b[1;32m    345\u001b[0m             parse_constant is None and object_pairs_hook is None and not kw):\n\u001b[0;32m--> 346\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0m_default_decoder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    347\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mcls\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/json/decoder.py\u001b[0m in \u001b[0;36mdecode\u001b[0;34m(self, s, _w)\u001b[0m\n\u001b[1;32m    336\u001b[0m         \"\"\"\n\u001b[0;32m--> 337\u001b[0;31m         \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mraw_decode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0midx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0m_w\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    338\u001b[0m         \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_w\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/json/decoder.py\u001b[0m in \u001b[0;36mraw_decode\u001b[0;34m(self, s, idx)\u001b[0m\n\u001b[1;32m    354\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 355\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mJSONDecodeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Expecting value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    356\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mJSONDecodeError\u001b[0m: Expecting value: line 1 column 1 (char 0)",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mJSONDecodeError\u001b[0m                           Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-26-0bbea5fd8b46>\u001b[0m in \u001b[0;36m<cell line: 13>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0mlast_date\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 13\u001b[0;31m \u001b[0;34m[\u001b[0m\u001b[0mcotacao\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m\"102023\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"092024\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     14\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[0mnosso_max\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmax\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-26-0bbea5fd8b46>\u001b[0m in \u001b[0;36m<listcomp>\u001b[0;34m(.0)\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0mlast_date\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 13\u001b[0;31m \u001b[0;34m[\u001b[0m\u001b[0mcotacao\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m\"102023\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"092024\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     14\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[0mnosso_max\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmax\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-26-0bbea5fd8b46>\u001b[0m in \u001b[0;36mcotacao\u001b[0;34m(data)\u001b[0m\n\u001b[1;32m      3\u001b[0m   \u001b[0murl\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34mf\"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?%40dataInicial='{data}'dataFinalCotacao='{data}'&%24format=json) \"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m   \u001b[0mres\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mrequests\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m   \u001b[0mres\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mres\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjson\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mcalendar\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/requests/models.py\u001b[0m in \u001b[0;36mjson\u001b[0;34m(self, **kwargs)\u001b[0m\n\u001b[1;32m    969\u001b[0m                     \u001b[0;32mpass\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    970\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mJSONDecodeError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 971\u001b[0;31m                     \u001b[0;32mraise\u001b[0m \u001b[0mRequestsJSONDecodeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdoc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpos\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    972\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    973\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mJSONDecodeError\u001b[0m: Expecting value: line 1 column 1 (char 0)"
          ]
        }
      ],
      "source": [
        "import requests\n",
        "def cotacao(data):\n",
        "  url = f\"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?%40dataInicial='{data}'dataFinalCotacao='{data}'&%24format=json) \"\n",
        "  res = requests.get(url)\n",
        "  res = res.json()\n",
        "\n",
        "import calendar\n",
        "from datetime import datetime\n",
        "first_date = datetime.strptime(\"102023\", \"%m%Y\")\n",
        "last_date = first_date.replace(day = calendar.monthrange(first_date.year, first_date.month)[1])\n",
        "last_date\n",
        "\n",
        "[cotacao(i) for i in [\"102023\", \"092024\"]]\n",
        "\n",
        "nosso_max = max(i)\n",
        "for i in i:\n",
        "  if (cotacao[i] == nosso_max):\n",
        "    print('Valor máximo dólar é %d' % cotacao[i])\n",
        "\n",
        "nosso_min = min(i)\n",
        "for i in i:\n",
        "  if (cotacao[i] == nosso_min):\n",
        "    print('Valor mínimo dólar é %d' % cotacao[i])\n",
        "def media(cotacao_dolar):\n",
        "  soma = sum(i)\n",
        "  return(soma / len(i))\n",
        "\n",
        "print('A Média da cotacão do dólar é:', media(i))\n",
        "\n",
        "\n"
      ]
    }
  ]
}