#include "app.h"
#include "logic.h"

App::App()
{
    menu();
}

App::~App() { }

void App::menu()
{
    draw_menu();
    new Logic();
}

void App::draw_menu()
{
    cout << "Whale Curve" << endl;
}