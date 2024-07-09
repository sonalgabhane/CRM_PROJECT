 'use strict';
module.exports = function (grunt) {

    // Load grunt tasks automatically
    require('load-grunt-tasks')(grunt);

    // Show grunt task time
    require('time-grunt')(grunt);

    // Configurable paths for the app
    var appConfig = {
        app: 'app',
        dist: 'dist',
        index: 'app/*.html'
    };

    // Grunt configuration
    grunt.initConfig({

        // Project settings
        applicator: appConfig,

        // Compile scss to css
        sass: {
            options: {
                sourceMap: false,
                noLineComments: true,
                outputStyle: 'compact'
            },
            dist: {
                files: {
                    "app/assets/css/app.css": "app/assets/scss/app.scss",
                    "app/assets/css/theme/theme-blue.css": "app/assets/scss/theme/theme-blue.scss"
                }
            },
        },
        // Watch for changes in live edit
        watch: {
            
            styles: {
                files: ['app/assets/scss/**/*.{scss,sass}']
            },
       
            js: {
                files: ['<%= applicator.app %>/scripts/{,*/}*.js']
            },
            sass: {
                files: ['app/assets/scss/**/*.{scss,sass}'],
                tasks: ['sass']
            },
            bower: {
                files: ['bower.json'],
                tasks: ['wiredep']
            }
        },
        wiredep : {
            dev : {
                directory : '../bower_components',
                src : [ '<%= applicator.index %>' ]
            }
        },
 
        uglify: {
            options: {
                mangle: false
            }
        },
        // Clean dist folder
        clean: {
            dist: {
                files: [{
                    dot: true,
                    src: [
                        '.tmp',
                        '<%= applicator.dist %>/{,*/}*',
                        '!<%= applicator.dist %>/.git*'
                    ]
                }]
            },
            server: '.tmp'
        },
        // Copies remaining files to places other tasks can use
        copy: {
            dist: {
                files: [
                    {
                        expand: true,
                        dot: true,
                        cwd: '<%= applicator.app %>',
                        dest: '<%= applicator.dist %>',
                        src: [
                            '*.{ico,png,jpg,jpeg,txt}',
                            '.htaccess',
                            '*.html',
                            'assets/fonts/*.*',
                            'assets/vendor/**',
                            'assets/css/**/{,*/}*.css',
                            'assets/js/**/{,*/}*.js',
                            'assets/images/**'
                        ]
                    }
                ]
            },
            styles: {
                expand: true,
                cwd: '<%= applicator.app %>/styles',
                dest: '.tmp/styles/',
                src: '{,*/}*.css'
            }
        },
        // Renames files for browser caching purposes
        filerev: {
            dist: {
                src: [
                    '<%= applicator.dist %>/assets/js/{,*/}*.js',
                    '<%= applicator.dist %>/assets/css/{,*/}*.css',
                    '<%= applicator.dist %>/assets/fonts/*',
                    '<%= applicator.dist %>/assets/vendor/*',
                    '<%= applicator.dist %>/assets/images/*'
                ]
            }
        },
        useminPrepare: {
            html: 'app/*.html',
            options: {
                dest: 'dist'
            }
        },
        usemin: {
            html: ['dist/*.html']
        }
    });
    // Run live version of app
    grunt.registerTask('live', [
        'clean:server',
        'copy:styles',
        'sass:dist',
        'connect:livereload',
        'watch'
    ]);
    
    // Run build version of app
    grunt.registerTask('server', [
        'build',
        'connect:dist:keepalive'
    ]);

    // Build version for production
    grunt.registerTask('build', [
        'clean:dist',
        'sass',
        'useminPrepare',
        'concat',
        'copy:dist',
        'uglify',
        'usemin'
    ]);
};
