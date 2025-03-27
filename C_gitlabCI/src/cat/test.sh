#!/bin/bash
COUNTER_SUCCESS=0
COUNTER_FAIL=0
DIFF_RES=""
TEST_FILE="Makefile"
echo "" > log.txt

for var in -b -e -n -s -t -E -T -v
do
          TEST1="$var $test_5_cat.txt"
          echo "$TEST1"
          ./s21_cat test_5_cat.txt > s21_cat.txt
          cat test_5_cat.txt > cat.txt
          DIFF_RES="$(diff -s s21_cat.txt cat.txt)"
          if [ "$DIFF_RES" == "Files s21_cat.txt and cat.txt are identical" ]
            then
              (( COUNTER_SUCCESS++ ))
              echo "$COUNTER_SUCCESS"
            else
              echo "test_5_cat.txt" >> log.txt
              (( COUNTER_FAIL++ ))
              echo "$COUNTER_FAIL"
          fi
           rm s21_cat.txt cat.txt
done

echo "Success: $COUNTER_SUCCESS"
echo "Fail: $COUNTER_FAIL"
