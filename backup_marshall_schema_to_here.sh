# USE THJS SCRIPT TO BACKUP THE MARSHALL SCHEME FROM THE DATABASE CURRENTLY LIVING ON MY MAC
cd ~/git_repos/_webapps_/marshall_webapp/marshall_webapp/tests/input
/usr/local/mysql/bin/mysql -u marshall --password=mar5ha11 marshall -e "update meta_workflow_lists_counts set count = 0"
echo "please give password for the marshall user"
/usr/local/mysql/bin/mysqldump -u marshall --password=mar5ha11 --no-data --routines marshall > marshall_schema.sql
echo "please give password for the marshall user again"
/usr/local/mysql/bin/mysqldump -u marshall --password=mar5ha11  marshall meta_workflow_lists_counts webapp_users marshall_fs_column_map stats_ssdr1_overview  stats_ssdr2_overview stats_ssdr3_overview >> marshall_schema.sql
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
