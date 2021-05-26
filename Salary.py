{
 "metadata": {
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
   "version": "3.9.5"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python395jvsc74a57bd007edb7e7d0660e2311268acf31f4ba32341e08f0f9d7eea147a5ab291842730e",
   "display_name": "Python 3.9.5 64-bit"
  },
  "metadata": {
   "interpreter": {
    "hash": "07edb7e7d0660e2311268acf31f4ba32341e08f0f9d7eea147a5ab291842730e"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Tax paid= 180000.0\nSalary after tax= 1020000.0\n"
     ]
    }
   ],
   "source": [
    "sal=1200000\n",
    "tax=0\n",
    "if sal<=300000:\n",
    "    print(\"No Income tax\")\n",
    "    print(\"Salary =\",sal)\n",
    "elif (sal>300000 and sal<500000):\n",
    "    tax=sal*(5/100)\n",
    "    sal=sal-tax\n",
    "    print(\"Tax paid=\",tax)\n",
    "    print(\"Salary after tax=\",sal)\n",
    "elif (sal>500000 and sal<1000000):\n",
    "    tax=sal*(10/100)\n",
    "    sal=sal-tax\n",
    "    print(\"Tax paid=\",tax)\n",
    "    print(\"Salary after tax=\",sal)\n",
    "elif (sal>1000000 and sal<1500000):\n",
    "    tax=sal*(15/100)\n",
    "    sal=sal-tax\n",
    "    print(\"Tax paid=\",tax)\n",
    "    print(\"Salary after tax=\",sal)\n",
    "elif (sal>1500000 and sal<2000000):\n",
    "    tax=sal*(20/100)\n",
    "    sal=sal-tax\n",
    "    print(\"Tax paid=\",tax)\n",
    "    print(\"Salary after tax=\",sal)\n",
    "else:\n",
    "    tax=sal*(25/100)\n",
    "    sal=sal-tax\n",
    "    print(\"Tax paid=\",tax)\n",
    "    print(\"Salary after tax=\",sal)"
   ]
  }
 ]
}