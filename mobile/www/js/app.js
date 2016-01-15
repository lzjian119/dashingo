// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('starter', ['ionic', 'starter.controllers'])

  .run(function ($ionicPlatform) {
    $ionicPlatform.ready(function () {
      if (window.cordova && window.cordova.plugins.Keyboard) {
        // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
        // for form inputs)
        cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);

        // Don't remove this line unless you know what you are doing. It stops the viewport
        // from snapping when text inputs are focused. Ionic handles this internally for
        // a much nicer keyboard experience.
        cordova.plugins.Keyboard.disableScroll(true);
      }
      if (window.StatusBar) {
        StatusBar.styleDefault();
      }
    });
  })

  .config(function ($stateProvider, $urlRouterProvider, $ionicConfigProvider) {

    $ionicConfigProvider.tabs.position('bottom');

    $stateProvider

      .state('app', {
        url: '/app',
        abstract: true,
        templateUrl: 'templates/app/menu.html',
        controller: 'AppCtrl'
      })

      .state('app.tab', {
        url: '/tab',
        views: {
          'main-content': {
            templateUrl: 'templates/app/tabs.html'
          }
        }
      })

      .state('app.tab.home', {
        url: '/home',
        views: {
          'tab-home': {
            templateUrl: 'templates/app/tab-home.html',
            controller: 'HomeCtrl'
          }
        }
      })

      .state('app.tab.square', {
        url: '/square',
        views: {
          'tab-square': {
            templateUrl: 'templates/app/tab-square.html',
            controller: 'SquareCtrl'
          }
        }
      })

      .state('app.tab.trend', {
        url: '/trend',
        views: {
          'tab-trend': {
            templateUrl: 'templates/app/tab-trend.html',
            controller: 'TrendCtrl'
          }
        }
      })

      .state('app.tab.activity', {
        url: '/activity',
        views: {
          'tab-activity': {
            templateUrl: 'templates/app/tab-activity.html',
            controller: 'ActivityCtrl'
          }
        }
      })

    // if none of the above states are matched, use this as the fallback
    $urlRouterProvider.otherwise('/app/tab/home');
  });
