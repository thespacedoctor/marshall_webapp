# USE THJS SCRIPT TO BACKUP THE MARSHALL SCHEME FROM THE DATABASE CURRENTLY LIVING ON MY MAC
cd ~/git_repos/_webapps_/marshall_webapp/marshall_webapp/tests/input
mysqldump -u marshall --password=mar5ha11 -h10.131.21.162 --port=9001 --no-data --routines marshall > marshall_schema.sql
mysqldump -u marshall --password=mar5ha11 -h10.131.21.162 --port=9001 marshall meta_workflow_lists_counts webapp_users stats_ssdr1_overview  stats_ssdr2_overview stats_ssdr3_overview marshall_fs_column_map >> marshall_schema.sql
perl -p -i.bak -e "s/DEFINER=\`\w.*?\`@\`.*?\`//g" marshall_schema.sql
perl -p -i.bak -e "s/ALTER DATABASE .*?CHARACTER.*?;//g" marshall_schema.sql
perl -p -i.bak -e "s/AUTO_INCREMENT=\d*//g"  marshall_schema.sql
rm -rf marshall_schema.sql.bak

echo "want to clear out unit_tests marshall database? [y|n]:"

read moveON

if [[ $moveON != "y" ]]
then
    exit
fi

mysql -u utuser --password=utpass unit_tests < marshall_schema.sql


