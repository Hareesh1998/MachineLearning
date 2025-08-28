{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPtp0SbhAntbjGmmLBMrrZl",
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
        "<a href=\"https://colab.research.google.com/github/Hareesh1998/MachineLearning/blob/main/python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f5XHy9wgTNv1",
        "outputId": "92652414-6c32-4697-8411-b5f4e68367a0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'HR': ['Alice', 'David'], 'IT': ['Bob', 'Charlie']}\n"
          ]
        }
      ],
      "source": [
        "from collections import defaultdict\n",
        "from os import name\n",
        "Employees = [\n",
        "    {'name' : 'Alice', 'department' : 'HR'},\n",
        "    {'name' : 'Bob', 'department' : 'IT'},\n",
        "    {'name' : 'Charlie', 'department' : 'IT'},\n",
        "    {'name' : 'David', 'department' : 'HR'}\n",
        "]\n",
        "\n",
        "grouped = {}\n",
        "for Employee in Employees:\n",
        "  grouped.setdefault(Employee['department'], []).append(Employee['name'])\n",
        "print(grouped)\n",
        "\n",
        "#{'HR': ['Alice', 'David'], 'IT': ['Bob', 'Charlie']}"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "year = int(input(\"enter the year: \"))\n",
        "if year > 0:\n",
        "  print(\"You have Entered: \",year)\n",
        "  if year % 4 == 0:\n",
        "    print(\"This \", year, \"you have entered is a Leap Year\")\n",
        "  else:\n",
        "    Print(\"This \", year, \"You have entered is not a Leap Year\")\n",
        "else:\n",
        "  print(\"Incorrect Year information\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MO0j8r9hx_dv",
        "outputId": "4fcdbce0-4e7c-4c6d-dbf7-4d875c524aa1"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the year: 2024\n",
            "You have Entered:  2024\n",
            "This  2024 you have entered is a Leap Year\n"
          ]
        }
      ]
    }
  ]
}