#include <iostream>
#include <fstream>
#include <dirent.h>
#include <algorithm>
#include <stdio.h>

#include <string>

#include "json.hpp"

using namespace std;


using json = nlohmann::json;




template<size_t SIZE, class T> inline size_t array_size(T (&arr)[SIZE]) {
        return SIZE;
    }


std::vector<string>  getFiles(char* path) {
    std::vector<string> filenames;
    //int n = 0;
    DIR *dir;
    string x = "";
    struct dirent *ent;
    if((dir = opendir (path)) != NULL) {
            while ((ent = readdir (dir)) != NULL) {
                x = ent->d_name;
                if (x.find(".json") != std::string::npos)
                {
                    filenames.push_back(x);
                }
            }
    }
    return filenames;

}


//std::vector<string> getDiseases(std::string file) {
//
//    std::cout <<"start of diseases\n";
//    std::string a, b, c;
//    std::cout <<"a, b, c\n";
//    std::string fullpath = "C:\\Users\\Rokas\\Desktop\\jsonparser\\jsonparser\\files\\" + file;
//    std::cout <<fullpath <<"\n";
//    std::ifstream i(fullpath);
//    json j;
//    i >> j;
//    i.clear();

//    std::string type = j["type"];



 //   json result;


 //   return diseases;
//}



json assignment(std::string file) {

    std::cout <<"start of assignment\n";
    std::string a, b, c;
    std::cout <<"a, b, c\n";
    std::string fullpath = "C:\\Users\\Rokas\\Desktop\\jsonparser\\jsonparser\\files\\" + file;
    std::cout <<fullpath <<"\n";
    std::ifstream g(fullpath);
    json j;
    g >> j;
    g.clear();
    std::cout << file << "\n";

    std::string type = j["type"];

    std::cout << type << "\n\n";

    json result;
    std::vector<string> medicines;
    std::vector<string> diseases;
    std::vector<string> datelist;

    if (type == "collection")
    {
        int n = 0;
        auto entries = j["entry"];
        auto entry = entries[n];

        std::vector<string> diseases;


        bool locationset = false;
        while (entries[n] != nullptr) {
            //entry = entries[n];
            std::string restype = entries[n]["resource"]["resourceType"];


            //city, state
            //std::cout << "AAAAAAAAAAAAAAAAAAA:\n" << entries[n]["resource"]["extension"][2]["valueAddress"] <<"\n";

            if (!locationset) {
            std::string location = "";
            if (nullptr != entries[n]["resource"]["extension"][2]["valueAddress"]["city"]) {
                a = entries[n]["resource"]["extension"][2]["valueAddress"]["city"];

                location += a;
                std::cout <<"Aaaaaaaaa" << a <<"\n";
            }
            if (nullptr != entries[n]["resource"]["extension"][2]["valueAddress"]["state"]) {
                b = entries[n]["resource"]["extension"][2]["valueAddress"]["state"];
                location = location + ", " + b;
                locationset = true;
            }

            result["Location"] = location;

            }

            std::cout << "location ok\n";


            if (entries[n]["resource"]["extension"][0]["valueCodeableConcept"]["text"] == "race") {
                result["Race"] = entries[n]["resource"]["extension"][0]["valueCodeableConcept"]["coding"][0]["display"]; //race
            }

            std::cout << "race ok\n";

            if (restype == "Observation") {

                                    //date
                                   //contains death?
                    if (entries[n]["resource"]["valueCodeableConcept"]["text"] != nullptr) {
                        a = entries[n]["resource"]["valueCodeableConcept"]["text"]; //disease
                        result["Disease"] = a;
                        diseases.push_back(a);
                    }
                    std::cout << "disease ok\n";
                    if (entries[n]["resource"]["assertedDate"] != nullptr) {
                        b = entries[n]["resource"]["assertedDate"];
                        result["Date"] = b;

                    }
                    std::cout << "date ok\n";
                    if (entries[n]["resource"]["code"]["text"] != nullptr) {
                        c = entries[n]["resource"]["code"]["text"];
                        result["Dead"] = true;
                    }
                    std::cout << "ded ok\n";
            }
            else if (restype == "MedicationRequest") {

                if (entries[n]["resource"]["medicationCodeableConcept"]["text"] != nullptr) {
                    a = entries[n]["resource"]["medicationCodeableConcept"]["text"]; //medicine
                    medicines.push_back(a);
                }
                std::cout << "med ok\n";


            }
            else if (restype == "Condition") {
                    if (nullptr != entries[n]["resource"]["assertedDate"]) {
                        a = entries[n]["resource"]["assertedDate"];
                        a.erase(std::remove(a.begin(), a.end(), '-'), a.end());
                        datelist.push_back(a);

                    }

                    result["Date"] = a;
                    if (nullptr != entries[n]["resource"]["code"]["text"]) {
                        b = entries[n]["resource"]["code"]["text"];
                        diseases.push_back(b);
                    } //also disease



            }
            n++;
            //std::cout << entry << "\n\n";
            //wicked ass algorithm shit


        }
        sort( datelist.begin(), datelist.end() );
        datelist.erase( unique( datelist.begin(), datelist.end() ), datelist.end() );
        sort( diseases.begin(), diseases.end() );
        diseases.erase( unique( diseases.begin(), diseases.end() ), diseases.end() );


        result["DateList"] = datelist;
        result["DiseaseList"] = diseases;
        result["Medication"] = medicines;
        std::cout << "med2 ok\n";

    }
    return result;

}


int main()
{
    int n = 0;
    string x = "";
    char* path = "C:\\Users\\Rokas\\Desktop\\jsonparser\\jsonparser\\files";
    std::vector<string> filenames = getFiles(path);
    json results;
    int fileamount = filenames.size() ;
    for (int i = 0; i<fileamount; i++) {
        results[to_string(i)] = assignment(filenames.at(i));
    }
    //n++;


    //returning the file
    std::ofstream o("output.json");
    o << std::setw(4) << results << std::endl;
    return 0;

}
