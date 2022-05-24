package com.lyrym.izanami.events;

import com.lyrym.izanami.DBHandler.DB;
import com.lyrym.izanami.Izanami;
import net.minecraft.world.entity.player.Player;
import net.minecraftforge.event.entity.living.LivingDamageEvent;
import net.minecraftforge.event.entity.living.LivingDeathEvent;
import net.minecraftforge.event.entity.living.LivingHealEvent;
import net.minecraftforge.event.entity.living.LivingSpawnEvent;
import net.minecraftforge.event.entity.player.PlayerEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

@Mod.EventBusSubscriber(modid=Izanami.MOD_ID)
public class ModEvents {
    private static Logger logger = LogManager.getLogger();
    @SubscribeEvent
    public static void DamageListener(LivingDamageEvent event){
        logger.info("1");

        if(!event.getEntity().level.isClientSide()){
            logger.info("2");

            if(event.getEntity() instanceof Player){
                Player player = ((Player) event.getEntity());
                DB.UpdateProfile(Math.round(player.getHealth() - event.getAmount()));
                System.out.println(Math.round(player.getHealth() - event.getAmount()));

            }
        }

    }
    @SubscribeEvent
    public static void HealListener(LivingHealEvent event){
        if(!event.getEntity().level.isClientSide()){

        }
        if(event.getEntity() instanceof Player){
            Player player = ((Player) event.getEntity());
            DB.UpdateProfile(Math.round(player.getHealth() + event.getAmount()));
            System.out.println(Math.round(player.getHealth() + event.getAmount()));

        }
    }
    @SubscribeEvent
    public static void SpawnListener(PlayerEvent.PlayerRespawnEvent event){
        if(!event.getEntity().level.isClientSide()){

        }
        if(event.getEntity() instanceof Player){
            Player player = ((Player) event.getPlayer());
            DB.UpdateProfile(Math.round(player.getHealth()));
            System.out.println(Math.round(player.getHealth()));

        }
    }
    @SubscribeEvent
    public static void DeathListener(LivingDeathEvent event){
        if(!event.getEntity().level.isClientSide()){

        }
        if(event.getEntity() instanceof Player){
            Player player = ((Player) event.getEntity());
            DB.UpdateProfile(Math.round(player.getHealth()));
            System.out.println(Math.round(player.getHealth()));

        }
    }



}
