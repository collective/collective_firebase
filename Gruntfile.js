
var collect = require('grunt-collection-helper');

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    copy: {
      'default': {
        files: {
          'firebaseplonedemo/static/dist/': [
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
          collect.bower('angular').path('angular.js')
        ],
        tasks: ['copy:default']
      }
    }
  });

  // Load the task plugins.
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task(s).
  grunt.registerTask('default', ['copy:default']);

};
