#!/bin/bash

num1=$(<num1.txt)
num2=$(<num2.txt)

declare -a nums

nums=(num1 num2)

if [ "$#" == 0 ]; then
	echo "...none operator parameter..."
	echo "1) add"
	echo "2) sub"
	echo "3) div"
	echo "4) mul"
	read -p "select menu : " menu
	set $menu
fi

case $1 in
	1) op="add" 
		let val=${nums[0]}+${nums[1]};;
	2) op="sub" 
		let val=${nums[0]}-${nums[1]};;
	3) op="div" 
		let val=${nums[0]}/${nums[1]};;
	4) op="mul" 
		let val=${nums[0]}*${nums[1]};;
	*) exit 0;;
esac


echo ""
echo "num1 : $num1"
echo "num2 : $num2"
echo "op : $op"
echo "result : $val"


