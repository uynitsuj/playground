#include <iostream>
#include <vector>
using namespace std;
class Plant {
    int waterLevel;
    bool hasSunlight;
    string genus;

public:
    Plant(int waterIn, bool sunlightIn, string genusIn);
    virtual bool hasWater() = 0;
    void moveToShade() {
        hasSunlight = false;
    }
    void waterPlant(int volume) {
        waterLevel += volume;
    }
    int getWaterLevel() {
        return waterLevel;
    }
    bool getSunlight() {
        return hasSunlight;
    }
};

class Flower : public Plant {
    int numPetals;

public:
    Flower(string genusIn, int petalsIn);

    bool hasWater() override {
        return getWaterLevel() > 5;
    }
};

class Tree : public Plant {
    int numFruit;

public:
    Tree(string genusIn, int fruitsIn);

    bool hasWater() override {
        return getWaterLevel() > 25;
    }
};

class Greenhouse
{
    vector<Plant *> plants;
    bool isHealthy;

public:
    //adds plant to the greenhouse
    void buyPlant(Plant *);
    // EFFECTS: returns true if more than half of the plants in the greenhouse 
    // have enough water and have access to sunlight
    bool growingGreenhouse();
};

class Cactus : public Plant {
    int height;

public:
    Cactus(string genusIn, int heightIn);

    int hasWater() override {
        return getWaterLevel() > 25;
    }
};


int main(int argc, char const *argv[])
{
    Plant rose(3, true, "rosa");
    rose.moveToShade();
    Greenhouse g;
    g.buyPlant(&rose);
    return 0;
}

bool Greenhouse::growingGreenhouse(){
    int gsize = plants.size();
    int healthycounter=0;
    for(int i=0; i<gsize;i++){
        if(plants.at(i)->getSunlight() && plants.at(i)->hasWater()){
            healthycounter++;
        }
    }
    if(healthycounter > gsize/2){
        return true;
    }
    return false;
}
Tree::Tree(string genusIn, int fruitsIn): Plant(0,1, genusIn), numFruit(fruitsIn) {}