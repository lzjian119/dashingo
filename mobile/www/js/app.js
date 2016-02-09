// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('starter', ['ionic', 'starter.controllers','starter.services'])

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

  .config(function ($stateProvider, $urlRouterProvider, $ionicConfigProvider, $httpProvider) {

    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

    $ionicConfigProvider.tabs.position('bottom');

    $ionicConfigProvider.views.swipeBackEnabled(false);

    $stateProvider

      .state('auth', {
        url: "/auth",
        templateUrl: "templates/app/auth/auth.html",
        abstract: true,
        controller: 'AuthCtrl'
      })

      .state('auth.log_04', {
        url: '/log_04',
        templateUrl: 'templates/app/auth/log_04.html',
        controller: 'AuthCtrl'
      })

      .state('auth.log_01', {
        url: '/log_01',
        templateUrl: 'templates/app/auth/log_01.html',
        controller: 'AuthCtrl'
      })

      .state('auth.log_02', {
        url: '/log_02',
        templateUrl: 'templates/app/auth/log_02.html',
        controller: 'AuthCtrl'
      })

      .state('auth.log_03', {
        url: '/log_03',
        templateUrl: 'templates/app/auth/log_03.html',
        controller: 'AuthCtrl'
      })

      .state('auth.log_05', {
        url: '/log_05',
        templateUrl: 'templates/app/auth/log_05.html',
        controller: 'AuthCtrl'
      })

      .state('auth.log_06', {
        url: '/log_06',
        templateUrl: 'templates/app/auth/log_06.html',
        controller: 'AuthCtrl'
      })

      .state('auth.log_07', {
        url: '/log_07',
        templateUrl: 'templates/app/auth/log_07.html',
        controller: 'AuthCtrl'
      })

      .state('app', {
        url: '/app',
        abstract: true,
        templateUrl: 'templates/app/menu.html',
        controller: 'MenuCtrl'
      })

      .state('app.tab', {
        url: '/tab',
        views: {
          'main-content': {
            templateUrl: 'templates/app/tabs.html',
            controller: 'TabCtrl'
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

      .state('app.tab.load_path', {
        url: '/load_path',
        views: {
          'tab-home': {
            templateUrl: 'templates/app/common/load_path.html',
            controller: 'LoadPathCtrl'
          }
        }
      })

      .state('app.tab.issue_event', {
        url: '/issue_event',
        views: {
          'tab-home': {
            templateUrl: 'templates/app/common/issue_event.html',
            controller: 'IssueEventCtrl'
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

      .state('app.home', {
        url: '/home',
        views: {
          'main-content': {
            templateUrl: 'templates/app/home/main.html',
            controller: 'HomePageCtrl'
          }
        }
      })

      .state('app.home_other', {
        url: '/home_other',
        views: {
          'main-content': {
            templateUrl: 'templates/app/home/other.html',
            controller: 'HomePageCtrl'
          }
        }
      })

      .state('app.notify', {
        url: '/notify',
        views: {
          'main-content': {
            templateUrl: 'templates/app/notify/main.html',
            controller: 'NotifyCtrl'
          }
        }
      })

      .state('app.draft', {
        url: '/draft',
        views: {
          'main-content': {
            templateUrl: 'templates/app/draft/main.html'
          }
        }
      })

      .state('app.draft_detail', {
        url: '/draft_detail',
        views: {
          'main-content': {
            templateUrl: 'templates/app/draft/detail.html'
          }
        }
      })

      .state('app.setting', {
        url: '/setting',
        views: {
          'main-content': {
            templateUrl: 'templates/app/setting/main.html'
          }
        }
      })

      .state('app.auxiliary', {
        url: '/auxiliary',
        views: {
          'main-content': {
            templateUrl: 'templates/app/setting/auxiliary.html'
          }
        }
      })


      .state('app.blacklist', {
        url: '/blacklist',
        views: {
          'main-content': {
            templateUrl: 'templates/app/setting/blacklist.html'
          }
        }
      })

    // if none of the above states are matched, use this as the fallback

    $urlRouterProvider.otherwise('/auth/log_01');

  })

.constant('apiUrl', 'http://192.168.55.102/index.php')
