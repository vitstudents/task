// Top-level build file where you can add configuration options common to all sub-projects/modules.
buildscript {
    repositories {
        // Check that you have the following line (if not, add it):
        google()  // Google's Maven repository
    }
    dependencies {
        // Add this line
        classpath 'com.google.gms:google-services:4.3.13'
//        classpath 'com.google.dagger:hilt-android-gradle-plugin:2.30.1-alpha'
        classpath("androidx.navigation:navigation-safe-args-gradle-plugin:2.5.3")
    }
}


plugins {
    id 'com.android.application' version '7.4.0' apply false
    id 'com.android.library' version '7.4.0' apply false
    id 'org.jetbrains.kotlin.android' version '1.8.10' apply false
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
