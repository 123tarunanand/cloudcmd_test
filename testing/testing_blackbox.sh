python black-box/test_1.py
rm -r black-box/New\ Folder
echo "Status : Pass"

python black-box/test_2.py
rm -r black-box/Nest-1
echo "Status : Pass"

python black-box/test_3.py
rm test_3.py
echo "Status : Pass"

python black-box/test_4.py
mv test_4_sample.txt black-box/test_4_sample.txt
echo "Status : Pass"

python black-box/test_5.py
rm test_4_sample.txt
echo "Status : Pass"

python black-box/test_6.py
echo "Status : Pass"

echo "Run test_7.sh to test if cloudcommander runs on a remote instance"

python black-box/test_8.py
rm black-box/test_8_sample.txt
echo "Status : Pass"

python black-box/test_9.py
rm black-box/test_9_sample.txt.zip
echo "Status : Pass"

python black-box/tests10-rest/test_11.py
rm black-box/tests10-rest/test_11_sample.txt.tar.gz
echo "Status : Pass"

python black-box/tests10-rest/test_12.py
echo "Status : Pass"

python black-box/tests10-rest/test_13.py
echo "Status : Pass"

python black-box/tests10-rest/test_14.py
mv black-box/tests10-rest/test_14_copy.txt black-box/tests10-rest/test_14_sample.txt
echo "Status : Pass"

python black-box/tests10-rest/test_15.py
echo "Status : Pass"

python black-box/tests10-rest/test_16.py
echo "Status : Pass"

python black-box/tests10-rest/test_17.py
echo "Status : Pass"

python black-box/tests10-rest/test_18.py
echo "Status : Pass"

python black-box/tests10-rest/test_19.py
echo "Status : Pass"

python black-box/tests10-rest/test_20.py
rm black-box/tests10-rest/test_20_sample.txt
echo "Status : Pass"

python black-box/tests10-rest/test_21.py
echo "Status : Pass"

python black-box/tests10-rest/test_22.py
echo "Status : Pass"

python black-box/tests10-rest/test_23.py
echo "Status : Pass"

python black-box/tests10-rest/test_24.py
echo "Status : Pass"

python black-box/tests10-rest/test_25.py
mv black-box/tests10-rest/test_25_rename.txt black-box/tests10-rest/test_25_sample.txt
echo "Status : Pass"
