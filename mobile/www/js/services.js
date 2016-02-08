
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
