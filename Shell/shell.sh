
#!/bin/bash
echo "自动化打包执行ing～"
cd Desktop
file="miot-plugin-sdk"
aa="com.philips.light.dimmablew"
bb="philips.light.zystrip"
cn="com."
PS3="您选择的是："
if [ -e $file ]
then
# echo "文件存在"
cd miot-plugin-sdk
cd projects
# ls
read -p "请输入设备model: " mode  #提示用户输入mode
if [ -e $mode ]
then 
echo "model已存在"

else
echo "选择设备类型?"
select type in bright  brightCCT brightCCTColor;
do
   break 
done
git clone https://gitee.com/DevYoung/Milight.git $cn$mode
cd $cn$mode
cd src
cd Common
case $type in
    bright)
    echo "You have selected bright"
    
;;
    brightCCT)
    
echo "You have selected brightCCT"
    sed -i "" "s/${bb}/${mode}/g" CommonJS.js
;;
    brightCCTColor)
   
echo "You have selected brightCCTColor"
;;
esac

# cd $cn$mode
cd ../../
 sed -i "" "s/${aa}/${cn}${mode}/g" project.json

 cd ../../
 npm run publish $cn$mode
 echo "打包完成..."

fi

else
echo "文件不存在"
git clone https://github.com/MiEcosystem/miot-plugin-sdk.git
fi




