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

      .state('tab', {
        url: '/tab',
        abstract: true,
        templateUrl: 'templates/tabs.html'
      })

      .state('tab.home', {
        url: '/home',
        views: {
          'tab-home': {
            templateUrl: 'templates/tab-home.html',
            controller: 'HomeCtrl'
          }
        }
      })

      .state('tab.square', {
        url: '/square',
        views: {
          'tab-square': {
            templateUrl: 'templates/tab-square.html',
            controller: 'SquareCtrl'
          }
        }
      })
      //.state('tab.chat-detail', {
      //  url: '/chats/:chatId',
      //  views: {
      //    'tab-chats': {
      //      templateUrl: 'templates/chat-detail.html',
      //      controller: 'ChatDetailCtrl'
      //    }
      //  }
      //})

      .state('tab.trend', {
        url: '/trend',
        views: {
          'tab-trend': {
            templateUrl: 'templates/tab-trend.html',
            controller: 'TrendCtrl'
          }
        }
      })

      .state('tab.activity', {
        url: '/activity',
        views: {
          'tab-activity': {
            templateUrl: 'templates/tab-activity.html',
            controller: 'ActivityCtrl'
          }
        }
      })

    //.state('app', {
    //  url: '/app',
    //  abstract: true,
    //  templateUrl: 'templates/menu.html',
    //  controller: 'AppCtrl'
    //})
    //
    //.state('app.search', {
    //  url: '/search',
    //  views: {
    //    'menuContent': {
    //      templateUrl: 'templates/search.html'
    //    }
    //  }
    //})
    //
    //.state('app.browse', {
    //  url: '/browse',
    //  views: {
    //    'menuContent': {
    //      templateUrl: 'templates/browse.html'
    //    }
    //  }
    //})
    //.state('app.playlists', {
    //  url: '/playlists',
    //  views: {
    //    'menuContent': {
    //      templateUrl: 'templates/playlists.html',
    //      controller: 'PlaylistsCtrl'
    //    }
    //  }
    //})
    //
    //.state('app.single', {
    //  url: '/playlists/:playlistId',
    //  views: {
    //    'menuContent': {
    //      templateUrl: 'templates/playlist.html',
    //      controller: 'PlaylistCtrl'
    //    }
    //  }
    //});

    // if none of the above states are matched, use this as the fallback
    $urlRouterProvider.otherwise('/tab/home');
  });
