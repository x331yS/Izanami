package com.lyrym.izanami.events;

import com.lyrym.izanami.DBHandler.DB;
import com.lyrym.izanami.Izanami;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.food.Foods;
import net.minecraft.world.item.EnchantedGoldenAppleItem;
import net.minecraftforge.event.entity.living.*;
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
            DB.UpdateProfile(50);
            System.out.println(50);

        }
    }
    @SubscribeEvent
    public static void DeathListener(LivingDeathEvent event){
        if(!event.getEntity().level.isClientSide()){

        }
        if(event.getEntity() instanceof Player){
            Player player = ((Player) event.getEntity());
            DB.UpdateProfile(-100);
            System.out.println(-100);

        }
    }
    @SubscribeEvent
    public static void StartEatingListener(LivingEntityUseItemEvent.Start event){
        if(event.getEntity() instanceof Player){
            if(event.getItem().getItem().isEdible()){
                System.out.println("Eat Start");
            }
        }


    }

    @SubscribeEvent
    public static void StopEatingListener(LivingEntityUseItemEvent.Stop event){
        if(event.getEntity() instanceof Player) {
            if (event.getItem().getItem().isEdible()) {
                System.out.println("Eat Stop");
            }
        }
    }

    @SubscribeEvent
    public static void FinishEatingListener(LivingEntityUseItemEvent.Finish event){
        if(event.getEntity() instanceof Player) {
            if (event.getItem().getItem().isEdible()) {
                System.out.println("Eat End");
            }
        }
    }



}
