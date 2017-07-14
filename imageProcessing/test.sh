read infile

python detect_circles.py -i $infile

python rotate.py -i result0.png
python rotate.py -i result1.png
f="result2.jpg"
if [ ! -f "$f" ]; then
	python rotate.py -i result2.png
fi

python crop.py -i result_result0.png
python crop.py -i result_result1.png


if [ ! -f "$f" ]; then
	python crop.py -i result_result2.png
fi


python toWhite.py -i result0_c.png
python toWhite.py -i result1_c.png
if [ ! -f "$f" ]; then
	python toWhite.py -i result2_c.png
fi

mkdir ref
mv result0_f.png ref
mv result1_f.png ref
if [ ! -f "$f" ]; then
	mv result2_f.png ref
fi
