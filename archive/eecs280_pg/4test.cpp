#include <iostream>
using namespace std;
struct Tool {
    string type;
    int weight;
};

// REQUIRES: t_ptr points to a valid Tool object
//           weight_in >= 0
// MODIFIES: *t_ptr
// EFFECTS: initializes the tool to have a given type and weight
void Tool_init(Tool *t_ptr, string type_in, int weight_in){
    t_ptr->type = type_in;
    t_ptr->weight = weight_in;
}

// REQUIRES: t_ptr points to a valid Tool object
// EFFECTS: returns the tool type
string Tool_type(const Tool *t_ptr);

// REQUIRES: t_ptr points to a valid Tool object
// EFFECTS: returns the tool weight
int Tool_weight(const Tool *t_ptr);

//The following code defines an abstract data type for Toolbox.

const int MAX_TOOLS = 99;

struct Toolbox {
    int max_weight;
    int num_tools; // Starts at 0
    Tool tools[MAX_TOOLS];
};

// REQUIRES: b_ptr points to a valid Toolbox object.
//           0 <= max_weight_in <= 1000
// MODIFIES: *b_ptr
// EFFECTS: Initializes the toolbox to have a given max_weight. 
//          Each toolbox starts with no tools.
void Toolbox_init(Toolbox *b_ptr, int max_weight_in){
    
}

// REQUIRES: b_ptr points to a Toolbox object
// EFFECTS:  returns the current total weight of the toolbox
//          (i.e. the sum of weights of all of its tools)
int Toolbox_current_weight(const Toolbox *b_ptr){
    int cur_weight = 0;
    for(int i = 0; i<b_ptr->num_tools; i++){
    cur_weight += Tool_weight(b_ptr->tools+i);
    }
    return cur_weight;
}
bool Toolbox_addTool(Toolbox *b_ptr, Tool tool){
if (Toolbox_current_weight(b_ptr)+
Tool_weight(&tool) > b_ptr->max_weight
|| b_ptr->num_tools == MAX_TOOLS)
{
    return false;
}
*(b_ptr->tools+b_ptr->num_tools) = tool;
return true;
}
// REQUIRES: b_ptr points to a valid toolbox
//           requirements is a valid array of [length] strings
// EFFECTS: returns true if b_ptr contains all of the tools listed in 
//          requirements, and false otherwise.
bool Toolbox_meets_requirements(Toolbox *b_ptr, string requirements[], int length);

const int MAX_TOOLBOXES = 10;

struct Carpenter {
    int jobs_completed;
    int num_toolboxes;
    Toolbox toolboxes[MAX_TOOLBOXES];
};



// REQUIRES: c_ptr points to a valid carpenter that has at least one toolbox 
//           with every required tool, requirements is a valid array of 
//           [length] strings
// EFFECTS: returns the toolbox that has all the required tools specified in 
//          requirements.
//          If multiple toolboxes fulfill the requirements, return the toolbox 
//          with the least current weight.
Toolbox Carpenter_choose_toolbox(Carpenter *c_ptr, string requirements[], int length){
Toolbox lowest_valid_toolbox = c_ptr->toolboxes[0];
int cur_lowest_weight = Toolbox_current_weight(&lowest_valid_toolbox);
for(int i = 1; i<MAX_TOOLBOXES; i++){
    if(Toolbox_meets_requirements(c_ptr->toolboxes+i, requirements, length) && 
    Toolbox_current_weight(c_ptr->toolboxes+i) < cur_lowest_weight){
        lowest_valid_toolbox = *(c_ptr->toolboxes+i);
        cur_lowest_weight = Toolbox_current_weight(c_ptr->toolboxes+i);
    }
}
return lowest_valid_toolbox;
}

int main(int argc, char const *argv[])
{
    cout << "test4";
    return 0;
}
