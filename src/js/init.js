requirejs.config({
    baseUrl: '/src',
    paths: {
        'backbone': 'libs/backbone',
        'marionette': 'libs/backbone.marionette.min',
        'underscore': 'libs/underscore',
        'backbone.radio': 'libs/backbone.radio',
        'jquery': 'libs/jquery',
        
        'text': 'libs/text',
    },
});

require(['js/app'], function(App){
    window.app = new App();
    window.app.render();
})