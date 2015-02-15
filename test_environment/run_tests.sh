RESULTS=results.txt
EXECUTABLE=uoflinsort


make

foldername=`echo $eachStudent | rev | cut -d '/' -f 2 | rev`
rm -r output/$foldername
mkdir -p output/$foldername
valgrind ./$eachStudent$EXECUTABLE input/test1 output/$foldername/test1 > output/$foldername/valgrind.log 2>&1
echo "Results" > results/$foldername
for eachTest in input/*
do
testname=`echo $eachTest | rev | cut -d '/' -f 1 | rev`
./$EXECUTABLE $eachTest output/$foldername/$testname >out.txt 2>&1
if diff output/$foldername/$testname solutions/$testname > output/$foldername/$RESULTS$testname
then
echo "PASS "$testname >> results/$foldername
else
echo "FAIL "$testname >> results/$foldername
fi
done
done

