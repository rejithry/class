// Transform.cpp: implementation of the Transform class.





#include "Transform.h"

#include <iostream>

//Please implement the following functions:



// Helper rotation function.  

mat3 Transform::rotate(const float degrees, const vec3& axis) {

  float theta =  -1 * degrees * 0.0174532925;

  // YOUR CODE FOR HW1 HERE



  // You will change this return call

  float x = axis.x;

  float y = axis.y;

  float z = axis.z;







  mat3 crosspmatrix = mat3(0, -1*z , y, 

			   z, 0, -1* x,

			   -1*y, x, 0);

  mat3 tensormatrix = mat3(x*x, x*y, x*z,

			   x*y, y*y, y*z,

			   x*z, y*z, z*z);

  mat3 id = mat3(1,0,0,

		 0,1,0,

		 0,0,1);



  return id*cos(theta) + (1 - cos(theta))* tensormatrix + sin(theta) * crosspmatrix;



}







// Transforms the camera left around the "crystal ball" interface

void Transform::left(float degrees, vec3& eye, vec3& up) {

  vec3 u = glm::normalize(up);

  eye = rotate(degrees, u) * eye;

  // YOUR CODE FOR HW1 HERE

  /*mat3 roatematrix  = rotate(-1*degrees, eye);

    eye = roatematrix * eye;

    up =  roatematrix * up;

    printf("%.2f, %.2f, %.2f",eye.x, eye.y, eye.z);*/

}



// Transforms the camera up around the "crystal ball" interface

void Transform::up(float degrees, vec3& eye, vec3& up) {

  float theta =  -1*degrees * 0.0174532925;

  vec3 axis = glm::cross(eye, up);

  vec3 u = glm::normalize(axis);

  eye = rotate(degrees, u) * eye;

  up = rotate(degrees, u)  * up;

}



// Your implementation of the glm::lookAt matrix

mat4 Transform::lookAt(vec3 eye, vec3 up) {

  



  // You will change this return call

  return glm::transpose(glm::lookAt(eye,vec3(0,0,0),up));

}



Transform::Transform()

{



}



Transform::~Transform()

{



}
