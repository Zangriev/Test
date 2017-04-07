$test = wc -l ../monfichier.txt | awk ' {print $1} '

echo $test