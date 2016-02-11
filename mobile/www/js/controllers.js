angular.module('starter.controllers', ['baiduMap'])



  .controller('AppCtrl', function ($scope, $ionicModal, $timeout) {

    // With the new view caching in Ionic, Controllers are only called
    // when they are recreated or on app start, instead of every page change.
    // To listen for when this page is active (for example, to refresh data),
    // listen for the $ionicView.enter event:
    //$scope.$on('$ionicView.enter', function(e) {
    //});

    // Form data for the login modal
    $scope.loginData = {};

    // Create the login modal that we will use later
    $ionicModal.fromTemplateUrl('templates/login.html', {
      scope: $scope
    }).then(function (modal) {
      $scope.modal = modal;
    });

    // Triggered in the login modal to close it
    $scope.closeLogin = function () {
      $scope.modal.hide();
    };

    // Open the login modal
    $scope.login = function () {
      $scope.modal.show();
    };

    // Perform the login action when the user submits the login form
    $scope.doLogin = function () {
      console.log('Doing login', $scope.loginData);

      // Simulate a login delay. Remove this and replace with your login
      // code if using a login system
      $timeout(function () {
        $scope.closeLogin();
      }, 1000);
    };
  })

  .controller('MenuCtrl', function ($scope, $ionicSideMenuDelegate) {
    $scope.closeMenu = function () {
      $ionicSideMenuDelegate.toggleLeft();
    };
  })

  .controller('PlaylistsCtrl', function ($scope) {
    $scope.playlists = [
      {title: 'Reggae', id: 1},
      {title: 'Chill', id: 2},
      {title: 'Dubstep', id: 3},
      {title: 'Indie', id: 4},
      {title: 'Rap', id: 5},
      {title: 'Cowbell', id: 6}
    ];
  })

  .controller('HomeCtrl', function ($scope, $rootScope) {
    var longitude = 113.738487;
    var latitude = 34.361282;
    $scope.mapOptions = {
      center: {
        longitude: longitude,
        latitude: latitude
      },
      zoom: 15,
      navCtrl: true,
      city: 'Xinzheng',
      markers: [{
        longitude: longitude,
        latitude: latitude,
        icon: 'http://img.coolwp.com/wp-content/uploads/2015/04/48-map-marker.png',
        width: 48,
        height: 48,
        title: '在哪儿',
        content: '新郑市梨河镇'
      }]
    };
    $scope.hideFlag = false;
    $scope.toggleDetail = function () {
      $scope.hideFlag = !$scope.hideFlag;
    };
    $scope.check_state = function (index) {
      return $rootScope.state == $rootScope.runing_state;
    }
    $scope.endTravel = function(){
      $rootScope.state = $rootScope.waitting_state;
    }
  })

  .controller('SquareCtrl', function ($scope) {
    $scope.query = {
      value: ''
    };
    $scope.tab = 1;
    $scope.searched = false;
    $scope.searching = function() {
      return $scope.query.value;
    };
    $scope.search_result = function () {
      $scope.searched = true;
    };
    $scope.back = function () {
      $scope.searched = false;
    };
    $scope.clear = function () {
      $scope.query.value = '';
      $scope.searched = false;
    };
    $scope.select_tab = function (index) {
      $scope.tab = index;
    };
    $scope.selected = function (index) {
      return $scope.tab == index;
    };
  })


  .controller('HomePageCtrl', function ($scope) {
    $scope.query = {
      value: ''
    };
    $scope.tab = 1;
    $scope.searched = false;
    $scope.searching = function() {
      return $scope.query.value;
    };
    $scope.search_result = function () {
      $scope.searched = true;
    };
    $scope.back = function () {
      $scope.searched = false;
    };
    $scope.clear = function () {
      $scope.query.value = '';
      $scope.searched = false;
    };
    $scope.select_tab = function (index) {
      $scope.tab = index;
    };
    $scope.selected = function (index) {
      return $scope.tab == index;
    };
  })

  .controller('LoadPathCtrl', function ($scope) {
    $scope.tab = 1;
    $scope.select_tab = function (index) {
      $scope.tab = index;
    };
    $scope.selected = function (index) {
      return $scope.tab == index;
    };
  })

  .controller('TrendCtrl', function ($scope, $stateParams) {
  })

  .controller('TabCtrl', function ($scope, $rootScope, $state) {
    // 控制中间按钮
    // 0: 未开始
    var waiting = {
      'state' : 0,
      'imgSrc' : 'img/go.png'
    }
    // 1: 进行中
    var running = {
      'state' : 1,
      'imgSrc' : 'img/record_spirit.png'
    }
    // 2: 休息
    var resting = {
       'state' : 2,
       'imgSrc' : 'img/rest.png'
    }

    $rootScope.waitting_state = waiting;
    $rootScope.runing_state = running;
    $rootScope.resting_state = resting;

    $rootScope.state = waiting;

    $scope.change = function () {
      if ($rootScope.state == running)
      {
        $state.go('app.tab.issue_event');
      }
      $rootScope.state = running;
    }
  })

  .controller('IssueEventCtrl', function ($scope) {

  })

  .controller('NotifyCtrl', function ($scope,notifyProvider) {
      $scope.notifications = notifyProvider.fetchNotifications();
      $scope.delete = function(notification){
        var newNotifications = $scope.notifications;
        $scope.notifications = [];
          newNotifications.forEach(function (elem) {
            if(notification !== elem) $scope.notifications.push(elem);
        });
      }
  })

  .controller('AuthCtrl', function($scope, $state, $ionicConfig) {
    $scope.jump = function(index) {
      $state.go('auth.log_0'+index);
    }
  })

  .controller('walkthroughCtrl', function($scope, $ionicConfig) {

  })

  .controller('ActivityCtrl', function ($scope,$ionicSlideBoxDelegate) {
    
    $scope.settings = {
      enableFriends: true
    };
  });
