<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInitd8e4193ce7335f54643066d0cb0e716d
{
    public static $classMap = array (
        'Ps_FeaturedProducts' => __DIR__ . '/../..' . '/ps_featuredproducts.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->classMap = ComposerStaticInitd8e4193ce7335f54643066d0cb0e716d::$classMap;

        }, null, ClassLoader::class);
    }
}
