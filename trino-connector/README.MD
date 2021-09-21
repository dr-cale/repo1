# trino-connector Documentation

What is Trino?
Trino is an apache 2.0 licensed, distributed SQL query engine, which was forked from the original Presto project whose Github repo was called PrestoDB. As such, it was designed from the ground up for fast queries against any amounts of data. It supports any types of data sources including relational and non-relational sources via its connector architecture.

What is the history of Trino?
Trino is a hard fork of the widely popular open source Presto project which started out at Facebook, running large-scale interactive analytic queries against a 300PB data lake using Hadoop/HDFS-based clusters. Prior to building Presto, Facebook used Apache Hive. In November, 2013, Facebook open sourced Presto under the Apache 2 license, and made it available in the public GitHub code repository named “prestodb”. In early 2019, the hard fork named Trino was started by the creators of Presto who later became cofounder/CTOs of the commercial vendor Starburst. In the meantime, Presto became part of the openly governed Presto Foundation, hosted under the guidance and experience of The Linux Foundation. Trino has subsequently divereged from Presto. Many of the innovations the community is driving in Presto are not available in Trino. Today, only Presto, not Trino is running at companies like Facebook, Uber, Twitter, and Alibaba.

Why is Trino so fast?
As Trino is a hard fork of the original Presto project, it carries with it some of the original elements which make Presto so fast, namely the in-memory execution architecture. Prior to Presto, distributed query engines such as Hive were designed to store intermediate results to disk.

How does Trino work?
Trino is a distributed system that runs on Hadoop, and uses an architecture similar to massively parallel processing (MPP) databases. It has one coordinator node working with multiple worker nodes. Users submit SQL to the coordinator which uses query and execution engine to parse, plan, and schedule a distributed query plan across the worker nodes. It supports standard ANSI SQL, including complex queries, joins aggregations, and outer joins.

What is Apache Trino?
Apache Trino is a misnomer in that Trino is not a project hosted under the well-known Apache Software Foundation (ASF). Apache Incubator and top level projects are subject to the naming conventions “Apache [Project Name].” An example of which is Apache Mesos. Instead trino project which is a hard fork of Presto is with a vendor controlled non-profit called the Trino Software Foundation. It is not affiliated with any well-known project hosting organizations like ASF for The Linux Foundation. The misnomer may have arisen from the fact that most open source projects use the Apache 2.0 license, which trino is licensed with.

Is Trino OLAP?
Trino is an open source distributed SQL query engine. It is a hard fork of the original Presto project created by Facebook. It lets developers run interactive analytics against large volumes of data. With Trino, organizations can easily use their existing SQL skills to query data without having to learn new complex languages. The Trino architecture is quite similar to traditional online analytical processing (OLAP) systems using distributed computing architectures, in which one controller node coordinates multiple worker nodes.

What is the Trino Software Foundation?
The Trino Software Foundation is a non-profit corporation which is controlled by the cofounders of the commercial vendor Starburst. The Trino Software Foundation has the open source Trino project. It is a hard fork of the Presto project, which is separate and hosted by the Linux Foundation. From the trino website there’s only two sentences about the foundation: “The Trino Software Foundation (formerly Presto Software Foundation) is an independent, non-profit organization with the mission of supporting a community of passionate users and developers devoted to the advancement of the Trino distributed SQL query engine for big data. It is dedicated to preserving the vision of high quality, performant, and dependable software.” What is not mentioned is any form of charter or governance. These are tables stakes for Linux Foundation projects, where the project governance is central to the project.

What SQL does Trino use?
Trino, like the original Presto, is built with a familiar SQL query interface that allows interactive SQL on many data sources. Standard ANSI SQL semantics are supported, including complex queries, joins, and aggregations.

What Is A Trino database?
Trino’s distributed system runs on Hadoop/HDFS and other data sources. It uses a classic MPP model (massively parallel processing). The java-based system has a coordinator node (master) working in conjunction with a scalable set of worker nodes. Users send their SQL query through a client to the Trino coordinator which plans and schedules a distributed query plan across all its worker nodes. Trino and Presto are SQL query engines and thus are not databases by themselves. They do not store any data, but from a user perspective, Trino can appear as a database because it queries the connected data stores.

What is the difference between Presto and Trino?
There are technical innovations and differences between Presto and Trino that include:
– Presto is developed, tested, and runs at scale at Facebook, Uber, and Twitter
– Presto uses 6X less memory and repartitions 2X faster with project Aria
– “Presto on Spark” today can run massive batch ETL jobs.
– Presto today is 10X faster with project RaptorX, providing caching at multiple levels
– The Presto community is making Presto more reliable and scalable with multiple coordinators instead of the single point of failure of one coordinator node.  

Trino can query data where it is stored, without needing to move data into separate warehouse or analytics database. Queries are executed in parallel with the memory of distributed worker machines. Most results return in seconds of time. Whereas Trino is a new fork, Presto continues to be used by many well-known companies: Facebook, Uber, Twitter, AWS. Trino is vendor driven project, as it is hosted in a non-profit organization which is owned by the cofounders of the Trino vendor Starburst. In comparison, Presto is hosted by Presto Foundation, a sub-foundation under The Linux Foundation. There are multiple vendors who support Presto, including the Presto as a Service (SaaS) offerings: Ahana Cloud for Presto and AWS Athena, which is based on Presto, not Trino.

As the diagram below illustrates, Presto saves time by running queries in the memory of the worker machines, running operations on intermediate datasets in-memory which is much faster, instead of persisting them to disk. It also shuffles data amongst the workers as needed. This also obviates the writes to disk between the stages. Hive intermediate data sets are persisted to disk. Presto executes tasks in-memory.

Whereas the pipelining approach between Presto and Trino is shared, Presto has a number of performance innovations that are not in Trino such as caching.  For more about the differences, see the April 2021 talk by Facebook at PrestoCon Day, which describe what they, along with others like Ahana, are doing to push the technology forward.

Trino is a distributed SQL query engine that is used best for running interactive analytic workloads on your data lakes and data sources. It is used for similar use cases that the original Presto project was designed for. It allows you to query against many different data sources whether its HDFS, Postgres, MySQL, Elastic, or a S3 based data lake. Trino is built on Java and can also integrate with other third party data sources or infrastructure components.
