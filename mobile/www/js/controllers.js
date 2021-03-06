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

    $scope.popularUsers = [
      {
        'name': '施搭搭',
        'headImage': 'img/head.png'
      },
      {
        'name': '作死的小乌龟',
        'headImage': 'img/head.png'
      },
      {
        'name': '吉莹',
        'headImage': 'img/head.png'
      },
      {
        'name': '春雨贵如油',
        'headImage': 'img/head.png'
      }
    ];

    $scope.popularRoutes = [
      {
        'title':'秘密之旅',
        'when':'2015.11.02',
        'who':{
          'name':'春雨贵如湿哒哒',
          'headImage':'img/head.png'
        },
        'pics':['img/pic_1.png','img/pic_2.jpg','img/pic_3.jpg','img/pic_4.jpg']
      }
    ];

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


  .controller('HomePageCtrl', function ($scope,userInformation) {

    $scope.selfRoutes = userInformation.getAllRoutes();

    $scope.followings = userInformation.getFollowings();

    $scope.followers = userInformation.getFollowers();

    $scope.getGenderImage = function(gender){
      if (gender == 0)
        return 'img/manicon.png';
      else
        return 'img/womanicon.png';
    }

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

  .controller('LoadPathCtrl', function ($scope, userInformation) {

    $scope.selfRoutes = userInformation.getAllRoutes();

    $scope.recommendationRoutes = [
      {
        'title':'推荐行程',
        'when':'2015.11.02',
        'who':{
          'name':'天气棒棒哒',
          'headImage':'img/head.png'
        },
        'pics':['img/pic_1.png','img/pic_2.jpg','img/pic_3.jpg','img/pic_4.jpg']
      },
      {
        'title':'高分行程',
        'when':'2015.11.02',
        'who':{
          'name':'春雨贵如油',
          'headImage':'img/head.png'
        },
        'pics':['img/pic_1.png','img/pic_2.jpg','img/pic_3.jpg','img/pic_4.jpg']
      },
      {
        'title':'秘密之旅',
        'when':'2015.11.02',
        'who':{
          'name':'春雨贵如湿哒哒',
          'headImage':'img/head.png'
        },
        'pics':['img/pic_1.png','img/pic_2.jpg','img/pic_3.jpg','img/pic_4.jpg']
      }
    ];
    $scope.tab = 1;
    $scope.select_tab = function (index) {
      $scope.tab = index;
    };
    $scope.selected = function (index) {
      return $scope.tab == index;
    };
  })

  .controller('TrendCtrl', function ($scope, $stateParams) {
    $scope.trendRoutes = [
      {
        'title':'秘密之旅',
        'when':'2015.11.02',
        'who':{
          'name':'春雨贵如湿哒哒',
          'headImage':'img/head.png'
        },
        'pics':['img/pic_1.png','img/pic_2.jpg','img/pic_3.jpg','img/pic_4.jpg']
      }
    ];
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

  .controller('IssueEventCtrl', function ($scope, Camera, $ionicActionSheet, $timeout) {

    var _photolibrary = 0;
    var _camera = 1;
    var sourceType = _camera;


    $scope.photos = [];
    $scope.delete = function(photo) {
      var newPhotos = [];
      $scope.photos.forEach(function(elem){
        if(elem !== photo) newPhotos.push(elem);
      });
      $scope.photos = newPhotos;
    }

    $scope.getPhoto = function() {
      Camera.getPicture({ sourceType: sourceType}).then(function(imageURI) {
        console.log(imageURI);
        $scope.photos.push(imageURI)
      }, function(err) {
          console.err(err);
        });
    };

    $scope.showActionSheet = function() {

      // Show the action sheet
      var hideSheet = $ionicActionSheet.show({
        buttons: [
          { text: '拍照' },
          { text: '从相册中选取' }
        ],
        titleText: '选取照片',
        cancelText: '取消',
        cancel: function() {
            // add cancel code..
          },
        buttonClicked: function(index) {
          if (index == 0) sourceType = _camera;
          else sourceType = _photolibrary
          $scope.getPhoto();
          return true;
      }
      });

   // For example's sake, hide the sheet after two seconds
   $timeout(function() {
     hideSheet();
   }, 2000);

 };

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

    //for the gender , 0 is female, 1 is male
    $scope.signUp = {
      account: '',
      password: '',
      validate: '',
      userName: '',
      gender:'',
      age:'',
      weight:'',
      height:'',
    }

    $scope.isPickGender = false;

    $scope.womanImage = 'img/womanoff.png'

    $scope.manImage = 'img/manoff.png'

    $scope.isValidationForPhone = function(){
      return false;
    };

    $scope.selectFemale = function(){
      $scope.isPickGender = true;
      $scope.womanImage = 'img/womanon.png'
      $scope.signUp.gender = 0;
      if($scope.isPickGender)  $scope.manImage = 'img/manoff.png';
    }

    $scope.selectMale = function(){
      $scope.isPickGender = true;
      $scope.manImage = 'img/manon.png';
      $scope.signUp.gender = 1;
      if($scope.isPickGender) $scope.womanImage = 'img/womanoff.png'
    }

    $scope.isAgeValidate = function(){
      if ($scope.signUp.age != '') return true;
      else return false;
    }

    $scope.isShapeValidate = function(){
      if($scope.signUp.weight != '' && $scope.signUp.height != '') return true;
      else return false;
    }

    $scope.isUserNameValidate = function() {
      if ($scope.signUp.userName != '')
        return true;
      else
        return false;
    };

    $scope.completeSignUp = function(){
      $state.go('app.tab.home');
    }

    $scope.jump = function(index) {
      $state.go('auth.log_0'+index);
    }

  })

  .controller('LoginCtrl', function($scope) {

    $scope.user = {
      userAccount: '',
      userPassword: ''
    }

    $scope.validate = function(){
      if($scope.user.userPassword != '' && $scope.user.userAccount != '')
        return true;
      else
        return false;
    }

  })

  .controller('walkthroughCtrl', function($scope, $ionicConfig) {

  })

  .controller('ActivityCtrl', function ($scope,$ionicSlideBoxDelegate) {
    $scope.settings = {
      enableFriends: true
    };
  });
