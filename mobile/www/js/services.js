
// notify

angular.module('starter.services', [])

  .factory('notifyProvider',function(){
    return {
      fetchNotifications: function(){
        return [{
                  "who": "sunny大表姐",
                  "what": "赞了你的旅程",
                  "where": "上海",
                  "when": "2016.1.12 13:12",
                  "extra": {
                    "img": "img/notify_img_example.png",
                    "content": "春雨贵如施搭搭的旅程春日记"
                  }
                },
                {
                  "who": "sunny大表姐",
                  "what": "赞了你的旅程",
                  "where": "上海",
                  "when": "2016.1.12 13:11",
                  "extra": {
                    "img": "img/notify_img_example.png",
                    "content": "春雨贵如施搭搭的旅程春日记"
                  }
                }]
      }
    };
  })

  .factory('userInformation',function(){
    return {
      getAllRoutes: function(){
        return [
                {
                  'title':'秘密之旅',
                  'when':'2015.11.02',
                  'who':{
                    'name':'春雨贵如湿哒哒',
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
              ]
      },
      getFollowings: function(){
        return [
          {
            'name':'作死的小乌龟',
            'headImage':'img/head.png',
            'gender':0
          },
          {
            'name':'Mr.holiday',
            'headImage':'img/head.png',
            'gender':0
          },
          {
            'name':'Jying1994',
            'headImage':'img/head.png',
            'gender':1
          },
          {
            'name':'PK',
            'headImage':'img/head.png',
            'gender':0
          }
        ]
      },
      getFollowers: function(){
        return [
          {
            'name':'Jying1994',
            'headImage':'img/head.png',
            'gender':1
          },
          {
            'name':'春雨贵如湿哒哒',
            'headImage':'img/head.png',
            'gender':0
          },
          {
            'name':'作死的小乌龟',
            'headImage':'img/head.png',
            'gender':0
          },
          {
            'name':'Mr.holiday',
            'headImage':'img/head.png',
            'gender':0
          }
        ]
      }
    };
  })
