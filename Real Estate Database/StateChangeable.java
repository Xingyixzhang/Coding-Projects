package com.xingyi;

/**
 * Author: Xingyi Zhang
 * File Name: StateChangeable.java
 * Date: July 8, 2020
 * Summary: This a generic public interface file with a generic abstract method.
 */

public interface StateChangeable<T extends Enum<T>> {
    void changeState(T t);
}
