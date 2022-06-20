const gulp = require('gulp');
const imagemin = require('gulp-imagemin');
const concat = require('gulp-concat');
const terser = require('gulp-terser');
const sourcemaps = require('gulp-sourcemaps');
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');
const prefix  = require('gulp-autoprefixer');
const sass = require('gulp-sass');
const rename = require('gulp-rename');
const browserSync = require('browser-sync').create();
const { src, series, parallel, dest, watch } = require('gulp');

const vendorJsPath = 'js/vendor/**/*.js';
const customJsPath = 'js/custom/**/*.js';
const scssPath = 'scss/**/*.scss';



function imgTask() {
    return src('uploads/*').pipe(imagemin()).pipe(gulp.dest('images/'));
}

function vendorJsPathTask() {
    return src(vendorJsPath)
        .pipe(sourcemaps.init())
        .pipe(concat('vendor.js'))
        .pipe(terser())
        .pipe(sourcemaps.write('.'))
        .pipe(dest('js'));
}

function customJsPathTask() {
    return src(customJsPath)
        .pipe(sourcemaps.init())
        .pipe(concat('custom.js'))
        .pipe(terser())
        .pipe(sourcemaps.write('.'))
        .pipe(dest('js'));
}


function scssTask() {
    return src(scssPath)
        .pipe(sourcemaps.init())
        .pipe(
            sass({
                errorLogToCOnsole: true,
                outputStyle: 'compressed'
            })
        )
        .on('error',console.error.bind(console))
        .pipe(prefix('last 2 versions'))
        .pipe(rename({suffix:'.min'}))
        .pipe(sourcemaps.write('.'))
        .pipe(dest('css'));
}

function watchTask() {
    watch([vendorJsPath,customJsPath,scssPath], { interval: 1000 }, parallel( vendorJsPathTask,customJsPathTask,scssTask));
}

// function  browser_sync() {
//     browserSync.init({
//         server: {
//             baseDir: "./"
//         }
//     });
// }

exports.scssTask = scssTask;
exports.vendorJsPathTask = vendorJsPathTask;
exports.customJsPathTask = customJsPathTask;
exports.imgTask = imgTask;

exports.default = parallel(
    parallel( imgTask, vendorJsPathTask,customJsPathTask, scssTask),/*browser_sync,*/
    watchTask
);
