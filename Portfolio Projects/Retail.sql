CREATE TABLE Marketing_Campaign(
    ID INTEGER PRIMARY KEY,
    Year_Birth INTEGER,
    Education TEXT,
    Marital_Status TEXT,
    Income INTEGER,
    Kidhome INTEGER,
    Teenhome INTEGER,
    Dt_Customer DATE,
    Recency INTEGER,
    MntWines INTEGER,
    MntFruits INTEGER,
    MntMeatProducts INTEGER,
    MntFishProducts INTEGER,
    MntSweetProducts INTEGER,
    MntGoldProds INTEGER,
    NumDealsPurchases INTEGER,
    NumWebPurchases INTEGER,
    NumCatalogPurchases INTEGER,
    NumStorePurchases INTEGER,
    NumWebVisitsMonth INTEGER,
    AcceptedCmp3 INTEGER,
    AcceptedCmp4 INTEGER,
    AcceptedCmp5 INTEGER,
    AcceptedCmp1 INTEGER,
    AcceptedCmp2 INTEGER,
    Complaint INTEGER,
    Z_CostContact INTEGER,
    Z_Revenue INTEGER,
    Response INTEGER,
    Age INTEGER
); -- Created the table

select Id, sum(Income) from Marketing_Campaign where Year_Birth = 1957 group by ID; // This query will return the ID and the sum of Income for all records where the Year_Birth is 1957, grouped by ID.

update Marketing_Campaign
   ...> set Dt_Customer = substr(Dt_Customer, 7, 4) || '-' ||
   ...> substr(Dt_Customer, 4, 2) || '-' ||
   ...> substr(Dt_Customer, 1, 2); -- This query will update the Dt_Customer field to a new format (YYYY-MM-DD) by rearranging the substrings of the original date format.

select Dt_Customer from Marketing_Campaign limit 5; // This query will return the Dt_Customer field for the first 5 records in the Marketing_Campaign table, allowing you to verify the changes made by the previous update query. 
--Data Preprocessing
select count(*) from Marketing_Campaign;  -- Calculate the total number of customer encounters in the marketing campaign dataset 

select 'Wines' as Product, sum(MntWines) as Total_purchase from Marketing_Campaign 
   ...> union all
   ...> select 'Fish Products' as Product, sum(MntFishProducts) as Total_purchase from Marketing_Campaign
   ...> union all
   ...> select 'Meat Products' as Product, sum(MntMeatProducts) as Total_purchase from Marketing_Campaign
   ...> union all
   ...> select 'Sweet Products' as Product, sum(MntSweetProducts) as Total_purchase from Marketing_Campaign
   ...> union all
   ...> select 'Gold Products' as Product, sum(MntGoldProds) as Total_purchase from Marketing_Campaign     
   ...> union all
   ...> select 'Fruits' as Product, sum(MntFruits) as Total_purchase from Marketing_Campaign          
   ...> order by total_purchase desc; -- This query will calculate the total purchase amount for each product category (Wines, Fish Products, Meat Products, Sweet Products, Gold Products, Fruits) and return the results ordered by total purchase amount in descending order.

select Response,count(*) from Marketing_Campaign group by Response; -- This query will count the number of occurrences for each unique value in the Response field, grouping the results by Response.

select Education, Marital_Status,count(*) as Customer_Count from Marketing_Campaign
group by Education, Marital_Status
order by Education, Marital_Status desc; --Determine the distribution of customers based on their education 
level and marital status 

select avg(Income) as Average_Income from Marketing_Campaign
where Response = 1; --Identify the average income of customers who participated in the marketing campaign 

select 'Campaign1' as Campaign, sum(AcceptedCmp1) as Promotions from Marketing_Campaign
   ...> union all
   ...> select 'Campaign2' as Campaign, sum(AcceptedCmp2) as Promotions from Marketing_Campaign
   ...> union all
   ...> select 'Campaign3' as Campaign, sum(AcceptedCmp3) as Promotions from Marketing_Campaign
   ...> union all
   ...> select 'Campaign4' as Campaign, sum(AcceptedCmp4) as Promotions from Marketing_Campaign
   ...> union all
   ...> select 'Campaign5' as Campaign, sum(AcceptedCmp5) as Promotions from Marketing_Campaign;
--Calculate the total number of promotions accepted by customers in each campaign

select case
   ...> when Response = 0 then 'Not Accepted'
   ...> when Response = 1 then 'Accepted'
   ...> end as Camp_Response,
   ...> count(*) as Response_Count,
   ...> round(count(*) * 100.0 /(select count(*) from Marketing_Campaign),2) as Percentage
   ...> from Marketing_Campaign
   ...> group by Response; --Identify the distribution of customers' responses to the last campaign 

select Kidhome,count(*) as Count, round(count(*) * 100.0 /(select count(*) from Marketing_Campaign),2) as Percentage
   ...> from Marketing_Campaign
   ...> group by Kidhome
   ...> order by Kidhome asc;
 select Teenhome,count(*) as Count, round(count(*) * 100.0 /(select count(*) from Marketing_Campaign),2) as Percentage
   ...> from Marketing_Campaign
   ...> group by Teenhome      
   ...> order by Teenhome asc;
--Calculate the average number of children and teenagers in customers' households 

SELECT strftime('%Y','now') - Year_Birth AS CurrentAge,
    CASE
        WHEN strftime('%Y','now') - Year_Birth BETWEEN 18 AND 25 THEN '18-25'
        WHEN strftime('%Y','now') - Year_Birth BETWEEN 26 AND 35 THEN '26-35'
        WHEN strftime('%Y','now') - Year_Birth BETWEEN 36 AND 45 THEN '36-45'
        WHEN strftime('%Y','now') - Year_Birth BETWEEN 46 AND 55 THEN '46-55'
        ELSE '55+'
    END AS Age_Group
FROM Marketing_Campaign; --Create an Age column by subtracting year_birth from the current year  
--• Create Age_group columns based on the below condition: 
--WHEN Age BETWEEN 18 AND 25 THEN '18-25' 
--WHEN Age BETWEEN 26 AND 35 THEN '26-35' 
--WHEN Age BETWEEN 36 AND 45 THEN '36-45' 
--WHEN Age BETWEEN 46 AND 55 THEN '46-55' 
--ELSE '56+'

SELECT
    Age_Group,
    ROUND(AVG(NumWebVisitsMonth), 2) AS Avg_Visits_Per_Month
FROM
(
    SELECT
        CAST(strftime('%Y','now') AS INTEGER) - Year_Birth AS Age,
        CASE
            WHEN CAST(strftime('%Y','now') AS INTEGER) - Year_Birth BETWEEN 18 AND 25 THEN '18-25'
            WHEN CAST(strftime('%Y','now') AS INTEGER) - Year_Birth BETWEEN 26 AND 35 THEN '26-35'
            WHEN CAST(strftime('%Y','now') AS INTEGER) - Year_Birth BETWEEN 36 AND 45 THEN '36-45'
            WHEN CAST(strftime('%Y','now') AS INTEGER) - Year_Birth BETWEEN 46 AND 55 THEN '46-55'
            ELSE '56+'
        END AS Age_Group,
        NumWebVisitsMonth
    FROM Marketing_Campaign
)
GROUP BY Age_Group
ORDER BY Age_Group;
--Create an Age column by subtracting year_birth from the current year  
--• Create Age_group columns based on the below condition: 
--WHEN Age BETWEEN 18 AND 25 THEN '18-25' 
--WHEN Age BETWEEN 26 AND 35 THEN '26-35' 
--WHEN Age BETWEEN 36 AND 45 THEN '36-45' 
--WHEN Age BETWEEN 46 AND 55 THEN '46-55' 
--ELSE '56+' 
--• Determine the average number of visits per month for customers in each age group