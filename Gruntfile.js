
var collect = require('grunt-collection-helper');

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    copy: {
      'default': {
        files: {
          'plone_interact/static/dist/': [
            collect.bower('angular').path('angular.js'),
            collect.bower('angularFire').path('angularFire.js'),
            collect.bower('angular-elastic').path('elastic.js')
          ]
        }
      }
    },
    uglify: {
      'default': {
        files: {
          'plone_interact/static/dist/angular.min.js': [
            collect.bower('angular').path('angular.js')
          ]
        }
      }
    },
    watch: {
      options: {
        debounceDelay: 250
      },
      'default': {
        files: [
          collect.bower('angular').path('angular.js'),
          collect.bower('angularFire').path('angularFire.js'),
          collect.bower('angular-elastic').path('elastic.js')
        ],
        tasks: ['copy:default', 'uglify:default']
      }
    }
  });

  // Load the task plugins.
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task(s).
  grunt.registerTask('default', ['copy:default', 'uglify:default']);

};
