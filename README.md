# CSCI620 Big Data: Spotify Dataset Project

## Project Description

This is an ongoing project worked on for the course "CSCI620: Introduction to Big Data" at Rochester Institute of Technology (Semester code: Spring 2225).

The project consists of three phases and a final presentation, the phases are briefly described below:

1. Phase I: Select/create a large dataset, relational model for the dataset
2. Phase II: Document-oriented model for the dataset
3. Phase III: Datamining

This README file will only contain basic descriptions of each phases, for detailed write up of each phase, refer to the pdf write ups in the docs folder.

## Contributors

- Vinod Dalavai | vd1605
- Ramprasad Kokkula | rk1668
- Samson Zhang | sz7651

## Dataset

Our dataset contains information on one million playlists created by Spotify users. The dataset is sourced from Kaggle, which can be found [here](https://www.kaggle.com/datasets/adityak80/spotify-millions-playlist).

The complete dataset is stored across a thousand json files, with each file containing a thousand playlists, which totals to a million playlists.

Each of the json files follow the naming pattern of:

`mpd.slice.[starting playlist number] - [ending playlist number]`

For example, `mpd.slice.0-999` contains the first 1,000 playlists, note the use of 0-based numbering.

## Relational Model: ER Diagram

![ER Diagram]()


## Relational Model: Loading Data

The overview of data loading is explained in these steps:

1. The json files are read, and a single csv file containing all the data is created.
2. Specific columns from the csv file is used to create temporary csv files corresponding to each table of the schema.
3. Temporary tables are created, these tables do not have any constraints to make initial data loading easier.
4. The content of the temporary csv files is inserted into the corresponding temporary tables.
5. The temporary tables are used to create tables that match the actual schema.
6. The temporary csv files are deleted and the temporary tables are dropped.

