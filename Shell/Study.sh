
#!/bin/bash

aa=("A" "B" "C")
PS3="您的选择是："
echo "数组元素个数为: ${#aa[*]}"
echo "请输入您的选择："
select type in  ${aa[*]}
do
 case $type in
    A)
    echo "您选择了A"
  ;;
    B)
    echo "您选择了B"
  ;;
    C)
    echo "您选择了C"
  ;;
  esac
  break
 done