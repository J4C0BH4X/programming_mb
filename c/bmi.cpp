//
// Created by dschrimpsher on 6/27/20.
//
#include <stdio.h>

int main() {
  int age = 0;
  int weight_kg = 0;
  float height_m = 0.0f;
  float bmi;
  printf("Enter your age:");
  scanf("%d", &age);
  if (age >= 18 && age <= 64) {
    printf("Enter your weight in kg:");
    scanf("%d", &weight_kg);
    printf("Enter your height in meters:");
    scanf("%f", &height_m);
    bmi = (float)(weight_kg) / (height_m*height_m);
    printf("BMI: %.10f ", bmi);
    if (bmi < 19) {
      printf("You are underweight\n");
    }
    else if (bmi > 24) {
      printf("You are overweight\n");
    }
    else {
      printf("You are right were you should be\n");
    }
  }
  else {
    printf("BMI is not valid for your age group\n");
  }

  return 0;
}

